# main.py

from fastapi import FastAPI, UploadFile, File
from chroma_client import get_chroma_client, create_collection
from embedder import embed_text
from typing import List
import pdfplumber
import docx

app = FastAPI()
client = get_chroma_client()
collection = create_collection(client)

def read_text_from_file(file: UploadFile):
    if file.filename.endswith('.pdf'):
        with pdfplumber.open(file.file) as pdf:
            return " ".join([page.extract_text() for page in pdf.pages])
    elif file.filename.endswith('.docx'):
        doc = docx.Document(file.file)
        return " ".join([para.text for para in doc.paragraphs])
    elif file.filename.endswith('.txt'):
        return file.file.read().decode('utf-8')
    else:
        raise ValueError("Unsupported file type")

@app.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    # Read and process document text
    text = read_text_from_file(file)
    embedding = embed_text(text)

    # Ingest into ChromaDB
    collection.add({"text": text, "embedding": embedding})

    return {"status": "Document ingested successfully"}

@app.post("/query")
async def query_similar_documents(query: str, top_k: int = 5):
    # Generate embedding for the query
    query_embedding = embed_text(query)
    
    # Retrieve similar documents
    results = collection.query({"embedding": query_embedding}, top_k=top_k)
    return {"results": results}
