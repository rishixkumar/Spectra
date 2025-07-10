from fastapi import APIRouter

router = APIRouter()

@router.get("/users/ping")
def ping():
    return {"status": "ok"}