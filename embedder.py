# embedder.py

from sentence_transformers import SentenceTransformer

# Initialize the embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def embed_text(text):
    return model.encode(text).tolist()
