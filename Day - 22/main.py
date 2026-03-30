from fastapi import FastAPI, UploadFile, File
from fastapi import Form
from pydantic import BaseModel
import PyPDF2
import io
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# Load API key from .env file
load_dotenv()

# Create the FastAPI app
app = FastAPI(title="AI Resume Analyzer", version="1.0")

# ─── Endpoint 1: Health Check ───
@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API is running! 🚀"}

# ─── Endpoint 2: PDF Upload ───
@app.post("/extract-resume")
async def extract_resume(file: UploadFile = File(...)):
    
    # Step 1: Read the uploaded file into memory
    contents = await file.read()
    
    # Step 2: Convert raw bytes into a PDF reader
    # PyPDF2 needs a "file-like object" not raw bytes
    # io.BytesIO wraps the bytes so PyPDF2 can read it
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))
    
    # Step 3: Extract text from every page
    # Loop through all pages, grab text, join together
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Step 4: Return the extracted text
    return {
        "filename": file.filename,
        "pages": len(pdf_reader.pages),
        "text_preview": text[:500],  # first 500 chars as preview
        "full_text": text
    }
# ─── Endpoint 3: Scrape Job URL ───
@app.post("/scrape-job")
def scrape_job(job_url: str):
    try:
        # Step 1: Fetch the webpage
        # Like a browser visiting the URL and downloading the page
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(job_url, headers=headers, timeout=10)

        # Step 2: Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove noise
        for tag in soup(["script", "style", "nav", "footer",
                          "header", "aside", "advertisement"]):
            tag.decompose()

        # Target main job content specifically
        main_content = (
            soup.find("div", {"class": lambda x: x and "job-description" in x.lower()}) or
            soup.find("div", {"class": lambda x: x and "description" in x.lower()}) or
            soup.find("div", {"id": lambda x: x and "job" in x.lower()}) or
            soup.find("main") or
            soup.find("article") or
            soup.body
        )

        text = main_content.get_text(separator=" ")
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        clean_text = " ".join(lines)

        return {
            "url": job_url,
            "characters": len(clean_text),
            "text_preview": clean_text[:500],
            "full_text": clean_text[:5000]  # limit to 5000 chars for GPT
        }

    except Exception as e:
        return {"error": str(e)}
    
# ─── Endpoint 4: Analyze Resume vs Job ───
@app.post("/analyze")
async def analyze(resume_text: str, job_text: str):
    try:
        # Step 1: Load OpenAI client
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Step 2: Craft the prompt
        # The better the prompt, the better the analysis
        prompt = f"""
        You are an expert career coach and hiring manager.
        
        Analyze the following resume against the job description and provide:
        
        1. MATCH SCORE: A percentage (0-100%) of how well the resume matches the job
        2. STRENGTHS: Top 3 things the candidate has that match the job
        3. MISSING SKILLS: Top 5 skills/keywords from the job that are missing in the resume
        4. SUGGESTIONS: Top 3 specific improvements the candidate should make
        5. SUMMARY: 2-3 sentence overall assessment
        
        Return your response in this EXACT JSON format:
        {{
            "match_score": 75,
            "strengths": ["strength 1", "strength 2", "strength 3"],
            "missing_skills": ["skill 1", "skill 2", "skill 3", "skill 4", "skill 5"],
            "suggestions": ["suggestion 1", "suggestion 2", "suggestion 3"],
            "summary": "Overall assessment here"
        }}
        
        RESUME:
        {resume_text[:3000]}
        
        JOB DESCRIPTION:
        {job_text[:3000]}
        """

        # Step 3: Call GPT-3.5
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0  # consistent, factual responses
        )

        # Step 4: Extract the response text
        result = response.choices[0].message.content

        # Step 5: Parse JSON response from GPT
        import json
        analysis = json.loads(result)

        return analysis

    except Exception as e:
        return {"error": str(e)}
# ─── Endpoint 5: Full Analysis (All in One!) ───
@app.post("/full-analyze")
async def full_analyze(
    file: UploadFile = File(...),
    job_url: str = Form(""),
    job_text_override: str = Form("")
):
    try:
        # ── Step 1: Extract resume text from PDF ──
        contents = await file.read()
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))
        resume_text = ""
        for page in pdf_reader.pages:
            resume_text += page.extract_text()

        # ── Step 2: Get job description ──
        if job_text_override:
            job_text = job_text_override[:3000]
        else:
            headers = {"User-Agent": "Mozilla/5.0"}
            scrape_response = requests.get(job_url, headers=headers, timeout=10)
            soup = BeautifulSoup(scrape_response.text, "html.parser")
            for tag in soup(["script", "style", "nav", "footer",
                            "header", "aside", "advertisement"]):
                tag.decompose()
            main_content = (
                soup.find("div", {"class": lambda x: x and "job-description" in x.lower()}) or
                soup.find("div", {"class": lambda x: x and "description" in x.lower()}) or
                soup.find("div", {"id": lambda x: x and "job" in x.lower()}) or
                soup.find("main") or
                soup.find("article") or
                soup.body
            )
            text = main_content.get_text(separator=" ")
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            job_text = " ".join(lines)[:3000]

        # ── Step 3: Analyze with GPT-3.5 ──
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        prompt = f"""
        You are an expert career coach and ATS (Applicant Tracking System) analyzer.

        CRITICAL INSTRUCTIONS:
        - The resume text may have formatting issues due to PDF extraction
        - Look EVERYWHERE in the resume for skills — project descriptions, 
        bullet points, tech stacks listed after project titles
        - If a project demonstrates a skill, count it as having that skill
        - "RAG Pipeline" project = knows RAG systems
        - "LangChain ReAct Agent" project = knows agentic workflows
        - "OpenAI GPT-3.5" anywhere = knows LLMs
        - "ChromaDB, embeddings" = knows vector databases
        - Do NOT mark a skill as missing if it appears ANYWHERE in the resume

        Analyze the resume against the job description and provide:

        1. MATCH SCORE: percentage (0-100%) based on actual skills found
        2. STRENGTHS: Top 3 specific things from resume matching the job
        3. MISSING SKILLS: Only skills TRULY absent from the entire resume
        4. SUGGESTIONS: Top 3 actionable improvements
        5. SUMMARY: 2-3 sentence assessment

        Return EXACT JSON format:
        {{
            "match_score": 75,
            "strengths": ["strength 1", "strength 2", "strength 3"],
            "missing_skills": ["skill 1", "skill 2", "skill 3", "skill 4", "skill 5"],
            "suggestions": ["suggestion 1", "suggestion 2", "suggestion 3"],
            "summary": "Overall assessment here"
        }}

        RESUME:
        {resume_text[:3000]}

        JOB DESCRIPTION:
        {job_text[:3000]}
        """

        response_gpt = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        result = response_gpt.choices[0].message.content
        import json
        analysis = json.loads(result)

        # ── Step 4: Return everything together ──
        return {
            "filename": file.filename,
            "job_url": job_url,
            "resume_pages": len(pdf_reader.pages),
            "analysis": analysis
        }

    except Exception as e:
        return {"error": str(e)}