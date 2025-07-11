"""
init_db.py

This module provides a function to initialize the database schema for the FastAPI application.
It creates all tables defined in the SQLAlchemy models (currently only the User model).

- init_db: Creates all tables in the database using SQLAlchemy metadata.
"""
from app.models.user import Base
from app.core.database import engine
#------------------------------------------------------------------------


#------------------------------------------------------------------------
def init_db():
    """
    Initialize the database by creating all tables defined in the SQLAlchemy models.
    Uses the engine from core.database.
    """
    Base.metadata.create_all(bind=engine)
