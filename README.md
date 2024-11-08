# Retrieval-Augmented Generation (RAG) FastAPI Server
This project implements a lightweight FastAPI server for a Retrieval-Augmented Generation (RAG) system. The server ingests text documents (PDF, DOCX, TXT) and queries similar documents using ChromaDB with embeddings generated by the Sentence Transformers model.

# Features
Document ingestion: Upload PDF, DOCX, and TXT files to the server, which are processed and stored in ChromaDB.
Similarity search: Query the database for similar documents based on the text input.
# Prerequisites
Python 3.8+
pip (Python package manager)

# Install Dependencies
pip install -r requirements.txt

# Run the FastAPI Server
Once all dependencies are installed, you can run the FastAPI server:
uvicorn main:app --reload
 # Test the API
 can now test the API using the interactive Swagger UI provided by FastAPI:

Open your browser and navigate to http://127.0.0.1:8000/docs.
You will see the documentation for the two available endpoints:
POST /ingest: Upload a file (PDF, DOCX, or TXT) to ingest into the database.
POST /query: Submit a text query to search for similar documents.
