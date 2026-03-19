import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import tempfile
import uuid


# Page config
st.set_page_config(page_title="PDF Chat App", page_icon="📄")
st.title("💬 PDF Chat App")
st.write("Upload a PDF and ask questions about it!")

# API Key
openai_api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type="password",
    placeholder="sk-..."
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None

# PDF Upload
uploaded_file = st.sidebar.file_uploader("Upload PDF", type="pdf")

# Reset if new PDF uploaded
if uploaded_file:
    if uploaded_file.name != st.session_state.current_pdf:
        st.session_state.qa_chain = None
        st.session_state.messages = []
        st.session_state.current_pdf = uploaded_file.name
        st.rerun()

if uploaded_file and openai_api_key:
    if st.session_state.qa_chain is None:
        with st.spinner("Processing PDF..."):
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
                f.write(uploaded_file.read())
                temp_path = f.name

            # Load and split
            loader = PyPDFLoader(temp_path)
            pages = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = splitter.split_documents(pages)

            # Create embeddings and store
            os.environ["OPENAI_API_KEY"] = openai_api_key
            embeddings = OpenAIEmbeddings()

            # Create unique collection for each PDF
            collection_name = f"pdf_{uuid.uuid4().hex[:8]}"
            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings,
                collection_name=collection_name
            )

            # Build QA chain
            llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
            retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

            template = """Use the following context to answer the question.
If you don't know the answer, say you don't know.
Be concise and helpful.

Context: {context}
Question: {question}
Answer:"""

            prompt = PromptTemplate.from_template(template)

            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            st.session_state.qa_chain = (
                {"context": retriever | format_docs,
                 "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )

        st.sidebar.success(f"✅ {uploaded_file.name} processed! {len(chunks)} chunks created.")

# Add clear conversation button
if st.sidebar.button("🗑️ Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# Display chat history
if st.session_state.current_pdf == uploaded_file.name if uploaded_file else False:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Only show messages if PDF matches current
if not uploaded_file or uploaded_file.name != st.session_state.current_pdf:
    st.session_state.messages = []

# Chat input
if question := st.chat_input("Ask a question about your PDF..."):
    if not openai_api_key:
        st.warning("Please enter your OpenAI API key in the sidebar!")
    elif st.session_state.qa_chain is None:
        st.warning("Please upload a PDF first!")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        # Get answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = st.session_state.qa_chain.invoke(question)
                st.write(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )