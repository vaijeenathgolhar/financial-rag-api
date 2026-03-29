from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.document import Document
from app.services.document_service import extract_text
from app.services.rag_service import index_document
from app.utils.dependencies import require_role

router = APIRouter(prefix="/documents")

def get_db():
    db = SessionLocal()
    yield db



@router.post("/upload")
async def upload(
    file: UploadFile,
    db: Session = Depends(get_db),
    user=Depends(require_role("Analyst"))
):
    content = await file.read()
    text = extract_text(content)

    doc = Document(
        title=file.filename,
        company_name="TestCo",
        document_type="report",
        uploaded_by=user["sub"]
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    index_document(doc.id, text)

    return {"msg": "Uploaded", "doc_id": doc.id}



@router.get("/")
def get_docs(db: Session = Depends(get_db)):
    return db.query(Document).all()



@router.get("/search")
def search_docs(company_name: str, db: Session = Depends(get_db)):
    return db.query(Document).filter(
        Document.company_name == company_name
    ).all()


@router.get("/{doc_id}")
def get_doc(doc_id: int, db: Session = Depends(get_db)):
    return db.query(Document).filter(Document.id == doc_id).first()



@router.delete("/{doc_id}")
def delete_doc(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()

    if not doc:
        return {"error": "Not found"}

    db.delete(doc)
    db.commit()

    return {"msg": "Deleted"}