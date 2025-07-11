"""
crud_user.py

This module provides CRUD (Create, Read, Update, Delete) operations and password utilities for user management in the FastAPI application.

- get_user_by_email: Retrieve a user by email from the database.
- create_user: Create a new user with a hashed password.
- verify_password: Verify a plain password against a hashed password using bcrypt.
- pwd_context: Passlib context for password hashing and verification.
"""
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
#------------------------------------------------------------------------

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#------------------------------------------------------------------------
def get_user_by_email(db: Session, email: str):
    """
    Retrieve a user from the database by email.

    Args:
        db (Session): SQLAlchemy session.
        email (str): User's email address.

    Returns:
        User | None: User object if found, else None.
    """
    return db.query(User).filter(User.email == email).first()

#------------------------------------------------------------------------
def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database with a hashed password.

    Args:
        db (Session): SQLAlchemy session.
        user (UserCreate): User creation schema with email and password.

    Returns:
        User: The created User object.
    """
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#------------------------------------------------------------------------
def verify_password(plain_password, hashed_password):
    """
    Verify a plain password against a hashed password.

    Args:
        plain_password (str): The plain text password.
        hashed_password (str): The hashed password from the database.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password) 