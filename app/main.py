from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, documents, rag, roles

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(documents.router)
app.include_router(rag.router)
app.include_router(roles.router)

@app.get("/")
def root():
    return {"msg": "Financial RAG API Running"}