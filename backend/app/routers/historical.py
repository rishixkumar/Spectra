"""
historical.py (routers)

This module defines the API route for fetching historical price data from Polygon.io in the FastAPI application.

- /stock/{symbol}/history (GET): Fetch historical price data for a given stock symbol and date range.
"""
#------------------------------------------------------------------------
from fastapi import APIRouter, HTTPException, Query
from app.core.historical_data import get_historical_prices
#------------------------------------------------------------------------

router = APIRouter()
#------------------------------------------------------------------------
@router.get("/stock/{symbol}/history", tags=["Stock History"])
def historical_prices(
    symbol: str,
    timespan: str = Query("day", enum=["minute", "hour", "day", "week", "month", "quarter", "year"]),
    from_date: str = Query("2024-01-01"),
    to_date: str = Query("2025-07-10")
):
    """
    Fetch historical price data for a given stock symbol and date range.
    Args:
        symbol (str): The stock ticker symbol.
        timespan (str): The time granularity.
        from_date (str): Start date (YYYY-MM-DD).
        to_date (str): End date (YYYY-MM-DD).
    Returns:
        dict: Symbol, timespan, date range, and list of price data points.
    Raises:
        HTTPException: If the fetch fails.
    """
    try:
        data = get_historical_prices(symbol, timespan, from_date, to_date)
        return {"symbol": symbol, "timespan": timespan, "from": from_date, "to": to_date, "prices": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stock/{symbol}/history/summary", tags=["Stock History"])
def historical_summary(
    symbol: str,
    timespan: str = Query("day", enum=["minute", "hour", "day", "week", "month", "quarter", "year"]),
    from_date: str = Query("2024-01-01"),
    to_date: str = Query("2025-07-10")
):
    try:
        data = get_historical_prices(symbol, timespan, from_date, to_date)
        closes = [d["c"] for d in data if "c" in d]
        if not closes:
            return {"symbol": symbol, "timespan": timespan, "from": from_date, "to": to_date, "summary": {}}
        summary = {
            "min_close": min(closes),
            "max_close": max(closes),
            "avg_close": sum(closes) / len(closes)
        }
        return {"symbol": symbol, "timespan": timespan, "from": from_date, "to": to_date, "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
