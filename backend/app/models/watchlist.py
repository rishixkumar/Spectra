"""
watchlist.py

This module defines the SQLAlchemy Watchlist model for tracking user watchlists in the FastAPI application.

- Watchlist: Represents a user's stock watchlist entry, with user_id and stock_symbol fields.
- Base: Declarative base for SQLAlchemy models (imported from models package).
"""
from sqlalchemy import Column, Integer, ForeignKey, String
from . import Base
#------------------------------------------------------------------------


#------------------------------------------------------------------------
class Watchlist(Base):
    """
    SQLAlchemy model for the 'watchlists' table.

    Attributes:
        id (int): Primary key, unique watchlist entry ID.
        user_id (int): Foreign key referencing the user.
        stock_symbol (str): Stock symbol being watched.
    """
    __tablename__ = "watchlists"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    stock_symbol = Column(String, nullable=False) 