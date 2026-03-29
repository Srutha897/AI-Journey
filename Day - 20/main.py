from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import PyPDF2
import io
from dotenv import load_dotenv
import os

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