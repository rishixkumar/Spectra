"""
stock.py (routers)

This module defines the API routes for fetching stock summary data and chart URLs from Yahoo Finance in the FastAPI application.

- /stock/{symbol} (GET): Fetch stock summary data.
- /stock/{symbol}/chart (GET): Fetch a Yahoo Finance chart URL for the stock.
"""
from fastapi import APIRouter, HTTPException
from app.core.stock_data import get_stock_summary, get_stock_chart_image
#------------------------------------------------------------------------

router = APIRouter()

#------------------------------------------------------------------------
@router.get("/stock/{symbol}", tags=["Stock"])
def stock_summary(symbol: str):
    """
    Fetch summary data for a given stock symbol.
    Args:
        symbol (str): The stock ticker symbol.
    Returns:
        dict: Stock summary data from Yahoo Finance.
    Raises:
        HTTPException: If the fetch fails or Yahoo returns invalid data.
    """
    try:
        data = get_stock_summary(symbol)
        return data
    except ValueError as e:
        raise HTTPException(status_code=502, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#------------------------------------------------------------------------
@router.get("/stock/{symbol}/chart", tags=["Stock"])
def stock_chart(symbol: str):
    """
    Fetch a Yahoo Finance chart URL for a given stock symbol.
    Args:
        symbol (str): The stock ticker symbol.
    Returns:
        dict: Chart URL for embedding in the frontend.
    """
    url = get_stock_chart_image(symbol)
    return {"chart_url": url}
