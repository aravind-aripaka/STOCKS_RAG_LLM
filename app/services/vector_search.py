import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

pinecone.init(api_key=PINECONE_API_KEY)

def create_index(index_name: str, dimension: int):
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(name=index_name, dimension=dimension)
        print(f"Index '{index_name}' created.")

def search_index(index_name: str, query_vector: list, top_k: int = 5):
    index = pinecone.Index(index_name)
    results = index.query(vector=query_vector, top_k=top_k)
    return results
