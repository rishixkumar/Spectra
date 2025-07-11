"""
historical_data.py

This module provides a utility function to fetch historical price data for a given stock symbol from Polygon.io.

Functions:
- get_historical_prices: Fetches historical OHLCV price data for a stock symbol and date range.
"""

import os
import requests
from dotenv import load_dotenv

#------------------------------------------------------------------------
load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

#------------------------------------------------------------------------
def get_historical_prices(symbol: str, timespan: str = "day", from_date: str = "2024-01-01", to_date: str = "2025-07-10"):
    """
    Fetch historical price data for a given stock symbol from Polygon.io.

    Args:
        symbol (str): The stock ticker symbol (e.g., 'AAPL').
        timespan (str): The time granularity (minute, hour, day, week, month, quarter, year).
        from_date (str): Start date in YYYY-MM-DD format.
        to_date (str): End date in YYYY-MM-DD format.
    Returns:
        list: List of OHLCV price data points.
    Raises:
        Exception: If the API request fails.
    """
    url = (
        f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/{timespan}/{from_date}/{to_date}"
        f"?adjusted=true&sort=asc&limit=5000&apiKey={POLYGON_API_KEY}"
    )
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(f"Polygon API error: {resp.status_code} {resp.text}")
    data = resp.json()
    return data.get("results", [])
