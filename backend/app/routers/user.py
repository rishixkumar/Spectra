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
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
#------------------------------------------------------------------------
from app.schemas.user import UserCreate, UserRead
#------------------------------------------------------------------------
from app.core.database import SessionLocal
from app.core.crud_user import create_user, get_user_by_email, verify_password, pwd_context
from app.core.jwt import create_access_token
from app.models.user import User
import os
from pydantic import EmailStr
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
# JWT settings
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user

#------------------------------------------------------------------------
@router.post("/users/register", response_model=UserRead, tags=["User"])
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
@router.post("/users/login", tags=["User"])
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
@router.get("/users/ping", tags=["User"])
def ping():
    """
    Health check endpoint for the user service.
    Returns:
        dict: Status message.
    """
    return {"status": "ok"}

#------------------------------------------------------------------------
@router.get("/users/me", response_model=UserRead, tags=["User"])
def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Get the current user's profile.
    """
    return current_user

#------------------------------------------------------------------------
@router.put("/users/me", response_model=UserRead, tags=["User"])
def update_current_user(update: UserCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Update the current user's profile (email/password).
    """
    # Check if email is being changed and if new email is already taken
    if update.email != current_user.email:
        existing_user = get_user_by_email(db, update.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        current_user.email = update.email
    # Update password if changed
    if not verify_password(update.password, current_user.hashed_password):
        current_user.hashed_password = pwd_context.hash(update.password)
    db.commit()
    db.refresh(current_user)
    return current_user

#------------------------------------------------------------------------
@router.post("/users/logout", tags=["User"])
def logout(token: str = Depends(oauth2_scheme)):
    """
    Logout endpoint (stateless, for JWT just instruct client to delete token).
    """
    return {"message": "Logout successful. Please delete your token on the client."}