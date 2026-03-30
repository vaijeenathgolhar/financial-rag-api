from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from app.config import QDRANT_HOST, QDRANT_PORT, COLLECTION_NAME

model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)


def init_collection():
    # try getting collection, if not create it
    try:
        client.get_collection(COLLECTION_NAME)
    except Exception as e:
        print("Collection not found, creating new one...")
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config={"size": 384, "distance": "Cosine"}
        )


def split_text(text):
    # simple chunking (can improve later)
    chunk_size = 300
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks


def index_document(doc_id, text):
    init_collection()

    chunks = split_text(text)

    if not chunks:
        print("No content to index")
        return

    vectors = model.encode(chunks)

    points = []
    for i in range(len(vectors)):
        points.append({
            "id": doc_id * 1000 + i,
            "vector": vectors[i],
            "payload": {
                "doc_id": doc_id,
                "text": chunks[i]
            }
        })

    client.upsert(collection_name=COLLECTION_NAME, points=points)


def search(query):
    if not query:
        return []

    query_vector = model.encode(query)

    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=20
    )

    return results