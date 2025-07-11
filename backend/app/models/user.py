"""
user.py

This module defines the SQLAlchemy User model for the FastAPI application.

- User: Represents a user in the system, with id, email, and hashed_password fields.
- Base: Declarative base for SQLAlchemy models (imported from models package).
"""
from sqlalchemy import Column, Integer, String
from . import Base
#------------------------------------------------------------------------


#------------------------------------------------------------------------
class User(Base):
    """
    SQLAlchemy model for the 'users' table.

    Attributes:
        id (int): Primary key, unique user ID.
        email (str): Unique email address for the user.
        hashed_password (str): Hashed password for authentication.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
