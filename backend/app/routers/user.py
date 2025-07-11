"""
user.py (routers)

This module defines the API routes for user registration, login, and health check in the FastAPI application.

- /users/register: Register a new user with email and password.
- /users/login: Authenticate a user and return a JWT access token.
- /users/ping: Health check endpoint.

Each route uses dependency injection for database sessions and leverages CRUD and JWT utilities from the core modules.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
#------------------------------------------------------------------------
from app.schemas.user import UserCreate, UserRead
#------------------------------------------------------------------------
from app.core.database import SessionLocal
from app.core.crud_user import create_user, get_user_by_email, verify_password
from app.core.jwt import create_access_token
#------------------------------------------------------------------------

router = APIRouter()

#------------------------------------------------------------------------
def get_db():
    """
    Dependency that provides a SQLAlchemy database session.
    Yields:
        Session: SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#------------------------------------------------------------------------
@router.post("/users/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.
    Args:
        user (UserCreate): User registration data.
        db (Session): Database session (injected).
    Returns:
        UserRead: The created user (id and email).
    Raises:
        HTTPException: If the email is already registered.
    """
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

#------------------------------------------------------------------------
@router.post("/users/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Authenticate a user and return a JWT access token.
    Args:
        form_data (OAuth2PasswordRequestForm): Login form data (username/email and password).
        db (Session): Database session (injected).
    Returns:
        dict: Access token and token type.
    Raises:
        HTTPException: If authentication fails.
    """
    user = get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

#------------------------------------------------------------------------
@router.get("/users/ping")
def ping():
    """
    Health check endpoint for the user service.
    Returns:
        dict: Status message.
    """
    return {"status": "ok"}