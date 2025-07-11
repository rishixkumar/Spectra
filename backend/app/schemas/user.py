"""
user.py (schemas)

This module defines Pydantic schemas for user creation and reading in the FastAPI application.

- UserCreate: Schema for user registration input (email, password).
- UserRead: Schema for user output (id, email), with ORM mode enabled for SQLAlchemy integration.
"""
from pydantic import BaseModel, EmailStr
#------------------------------------------------------------------------


#------------------------------------------------------------------------
class UserCreate(BaseModel):
    """
    Schema for creating a new user.

    Attributes:
        email (EmailStr): User's email address.
        password (str): User's plain password (to be hashed).
    """
    email: EmailStr
    password: str

#------------------------------------------------------------------------
class UserRead(BaseModel):
    """
    Schema for reading user data (output).

    Attributes:
        id (int): User's unique ID.
        email (EmailStr): User's email address.
    """
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
