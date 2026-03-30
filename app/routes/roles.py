from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.role import Role

router = APIRouter(prefix="/roles")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
def create_role(role_name: str, db: Session = Depends(get_db)):
    """
    Create a new role in the system.
    Prevents duplicate roles.
    """

    existing_role = db.query(Role).filter(Role.name == role_name).first()

    if existing_role:
        raise HTTPException(status_code=400, detail="Role already exists")

    new_role = Role(name=role_name)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return {
        "msg": "Role created successfully",
        "role_id": new_role.id,
        "role_name": new_role.name
    }