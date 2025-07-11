"""
admin.py (routers)

This module defines admin endpoints for listing users and viewing logs.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.routers.user import get_current_user
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def require_admin(current_user: User = Depends(get_current_user)):
    """
    Dependency to ensure the current user is an admin.
    """
    if not getattr(current_user, 'is_admin', False):
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user

@router.get("/admin/users", tags=["Admin"])
def list_users(current_user: User = Depends(require_admin), db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "email": u.email} for u in users]

@router.get("/admin/logs", tags=["Admin"])
def view_logs(current_user: User = Depends(require_admin)):
    # Placeholder: return static logs
    return {"logs": ["Log entry 1", "Log entry 2"]} 