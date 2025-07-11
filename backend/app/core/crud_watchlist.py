"""
crud_watchlist.py

This module provides CRUD operations for managing user watchlists in the FastAPI application.

- get_watchlist: Retrieve all watchlist entries for a user.
- add_to_watchlist: Add a stock symbol to a user's watchlist.
- remove_from_watchlist: Remove a stock symbol from a user's watchlist.
"""
from sqlalchemy.orm import Session
from app.models.watchlist import Watchlist
from app.schemas.watchlist import WatchlistCreate
#------------------------------------------------------------------------


#------------------------------------------------------------------------
def get_watchlist(db: Session, user_id: int):
    """
    Retrieve all watchlist entries for a given user.
    Args:
        db (Session): SQLAlchemy session.
        user_id (int): The user's ID.
    Returns:
        list[Watchlist]: List of Watchlist entries for the user.
    """
    return db.query(Watchlist).filter(Watchlist.user_id == user_id).all()


#------------------------------------------------------------------------
def add_to_watchlist(db: Session, user_id: int, stock_symbol: str):
    """
    Add a stock symbol to a user's watchlist.
    Args:
        db (Session): SQLAlchemy session.
        user_id (int): The user's ID.
        stock_symbol (str): The stock symbol to add.
    Returns:
        Watchlist: The created Watchlist entry.
    """
    watch = Watchlist(user_id=user_id, stock_symbol=stock_symbol)
    db.add(watch)
    db.commit()
    db.refresh(watch)
    return watch

#------------------------------------------------------------------------
def remove_from_watchlist(db: Session, user_id: int, stock_symbol: str):
    """
    Remove a stock symbol from a user's watchlist.
    Args:
        db (Session): SQLAlchemy session.
        user_id (int): The user's ID.
        stock_symbol (str): The stock symbol to remove.
    Returns:
        Watchlist | None: The removed Watchlist entry, or None if not found.
    """
    watch = db.query(Watchlist).filter(
        Watchlist.user_id == user_id,
        Watchlist.stock_symbol == stock_symbol
    ).first()
    if watch:
        db.delete(watch)
        db.commit()
    return watch 