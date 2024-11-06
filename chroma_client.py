# chroma_client.py

from chromadb import Client
from chromadb.config import Settings

# Function to get a ChromaDB client with persistent storage
def get_chroma_client():
    # Use Settings to specify the persist directory
    settings = Settings(persist_directory="./chroma_storage")  # Directory to save data
    client = Client(settings=settings)
    return client

# Function to create or get a collection (like a "bucket" for documents)
def create_collection(client, collection_name="documents"):
    return client.get_or_create_collection(collection_name)

