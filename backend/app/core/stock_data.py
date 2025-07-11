"""
stock_data.py

This module provides functions to fetch stock summary data and chart URLs from Yahoo Finance for use in the FastAPI backend.

Functions:
- get_stock_summary: Fetches detailed stock summary data using yfinance.
- get_stock_chart_image: Constructs a Yahoo Finance chart URL for embedding in the frontend.
"""
import os
import requests
#------------------------------------------------------------------------
from dotenv import load_dotenv
load_dotenv()

#------------------------------------------------------------------------

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

def get_stock_summary(symbol: str):
    """
    Fetch summary data for a given stock symbol from Polygon.io.

    Args:
        symbol (str): The stock ticker symbol (e.g., 'AAPL').
    Returns:
        dict: Stock summary data from Polygon.io.
    Raises:
        ValueError: If the request fails or data is missing.
    """
    url = f"https://api.polygon.io/v3/reference/tickers/{symbol.upper()}?apiKey={POLYGON_API_KEY}"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError(f"Polygon.io API returned status {resp.status_code}: {resp.text[:200]}")
    data = resp.json()
    if "results" not in data:
        raise ValueError(f"No data found for symbol: {symbol}")
    return data["results"]

#------------------------------------------------------------------------

def get_stock_chart_image(symbol: str, period='1mo', interval='1d'):
    """
    Construct a Yahoo Finance chart URL for a given stock symbol.

    Args:
        symbol (str): The stock ticker symbol.
        period (str, optional): Chart period (unused, for future extension).
        interval (str, optional): Chart interval (unused, for future extension).
    Returns:
        str: URL to Yahoo Finance chart page for embedding.
    """
    chart_url = f"https://finance.yahoo.com/chart/{symbol}?p={symbol}"
    return chart_url  # Frontend can embed this as an iframe or image
