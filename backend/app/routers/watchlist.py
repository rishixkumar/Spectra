"""
watchlist.py (routers)

This module defines the API routes for managing user watchlists in the FastAPI application.

- /watchlist (GET): Retrieve the current user's watchlist.
- /watchlist (POST): Add a stock to the user's watchlist.
- /watchlist/{stock_symbol} (DELETE): Remove a stock from the user's watchlist.

Note: USER_ID is currently hardcoded for demonstration; replace with JWT user extraction in production.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.crud_watchlist import get_watchlist, add_to_watchlist, remove_from_watchlist
from app.schemas.watchlist import WatchlistCreate, WatchlistRead
from app.routers.user import get_current_user
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

# For demonstration, use a placeholder for user_id until JWT user extraction is added
USER_ID = 1


#------------------------------------------------------------------------
@router.get("/watchlist", response_model=list[WatchlistRead], tags=["Watchlist"])
def read_watchlist(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Retrieve the current user's watchlist.
    Args:
        db (Session): Database session (injected).
    Returns:
        list[WatchlistRead]: List of watchlist entries.
    """
    return get_watchlist(db, user_id=current_user.id)


#------------------------------------------------------------------------
@router.post("/watchlist", response_model=WatchlistRead, tags=["Watchlist"])
def add_stock_to_watchlist(item: WatchlistCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Add a stock to the user's watchlist.
    Args:
        item (WatchlistCreate): Stock symbol to add.
        db (Session): Database session (injected).
    Returns:
        WatchlistRead: The created watchlist entry.
    """
    return add_to_watchlist(db, user_id=current_user.id, stock_symbol=item.stock_symbol)

#------------------------------------------------------------------------
@router.delete("/watchlist/{stock_symbol}", status_code=204, tags=["Watchlist"])
def remove_stock_from_watchlist(stock_symbol: str, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Remove a stock from the user's watchlist.
    Args:
        stock_symbol (str): The stock symbol to remove.
        db (Session): Database session (injected).
    Raises:
        HTTPException: If the stock is not found in the watchlist.
    """
    removed = remove_from_watchlist(db, user_id=current_user.id, stock_symbol=stock_symbol)
    if not removed:
        raise HTTPException(status_code=404, detail="Stock not found in watchlist") 