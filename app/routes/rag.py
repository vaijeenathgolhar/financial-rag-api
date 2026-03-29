from fastapi import APIRouter
from app.services.rag_service import search

router = APIRouter(prefix="/rag")

@router.post("/search")
def semantic_search(query: str):
    results = search(query)

    return [
        {
            "score": r.score,
            "text": r.payload["text"]
        }
        for r in results
    ]