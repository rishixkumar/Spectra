"""
models/__init__.py

This module initializes the SQLAlchemy declarative base and imports all model classes for the FastAPI application.

- Base: Declarative base for all models.
- User: User model.
- Watchlist: Watchlist model.
"""
#------------------------------------------------------------------------
from sqlalchemy.orm import declarative_base
Base = declarative_base()

#------------------------------------------------------------------------
from .user import User
from .watchlist import Watchlist 