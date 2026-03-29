from fastapi import APIRouter

router = APIRouter(prefix="/roles")

@router.post("/create")
def create_role(role: str):
    return {"msg": f"Role {role} created"}