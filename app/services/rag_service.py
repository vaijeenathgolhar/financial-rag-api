from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from app.config import *

model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)


def init_collection():
    try:
        client.get_collection(COLLECTION_NAME)
    except:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config={"size": 384, "distance": "Cosine"}
        )


def split_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]


def index_document(doc_id, text):
    init_collection()

    chunks = split_text(text)
    vectors = model.encode(chunks)

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            {
                "id": i + doc_id * 1000,
                "vector": vectors[i],
                "payload": {
                    "doc_id": doc_id,
                    "text": chunks[i]
                }
            }
            for i in range(len(chunks))
        ]
    )


# ✅ ADD THIS (FIX)
def search(query):
    query_vector = model.encode(query)

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=20
    )

    return results