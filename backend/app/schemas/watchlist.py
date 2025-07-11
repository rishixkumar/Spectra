"""
watchlist.py (schemas)

This module defines Pydantic schemas for watchlist creation and reading in the FastAPI application.

- WatchlistCreate: Schema for adding a stock to a user's watchlist.
- WatchlistRead: Schema for reading a watchlist entry (id, stock_symbol).
"""
from pydantic import BaseModel
#------------------------------------------------------------------------


#------------------------------------------------------------------------
class WatchlistCreate(BaseModel):
    """
    Schema for creating a new watchlist entry.

    Attributes:
        stock_symbol (str): The stock symbol to add to the watchlist.
    """
    stock_symbol: str


#------------------------------------------------------------------------
class WatchlistRead(BaseModel):
    """
    Schema for reading a watchlist entry.

    Attributes:
        id (int): Unique ID of the watchlist entry.
        stock_symbol (str): The stock symbol in the watchlist.
    """
    id: int
    stock_symbol: str

    class Config:
        orm_mode = True 