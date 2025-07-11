"""
news.py (routers)

This module defines the API route for fetching company news from Finnhub in the FastAPI application.

- /news/{symbol} (GET): Fetch news articles for a given stock symbol.
"""
#------------------------------------------------------------------------
from fastapi import APIRouter, HTTPException
from app.core.news_data import get_news_for_symbol
#------------------------------------------------------------------------

router = APIRouter()
#------------------------------------------------------------------------
@router.get("/news/{symbol}", tags=["News"])
def news(symbol: str):
    """
    Fetch news articles for a given stock symbol.
    Args:
        symbol (str): The stock ticker symbol.
    Returns:
        list: News articles from Finnhub.
    Raises:
        HTTPException: If the news fetch fails.
    """
    try:
        data = get_news_for_symbol(symbol)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 