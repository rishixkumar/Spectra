"""
news_data.py

This module provides a utility function to fetch company news from Finnhub for a given stock symbol.

Functions:
- get_news_for_symbol: Fetches news articles for a stock symbol using Finnhub's API.
"""
#------------------------------------------------------------------------
import os
import requests
from dotenv import load_dotenv
#------------------------------------------------------------------------
load_dotenv()
#------------------------------------------------------------------------
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

def get_news_for_symbol(symbol: str):
    """
    Fetch news articles for a given stock symbol from Finnhub.

    Args:
        symbol (str): The stock ticker symbol (e.g., 'AAPL').
    Returns:
        list: List of news articles (dicts) from Finnhub.
    Raises:
        Exception: If the API request fails.
    """
    url = f"https://finnhub.io/api/v1/company-news?symbol={symbol}&from=2024-01-01&to=2025-07-10&token={FINNHUB_API_KEY}"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(f"Finnhub News API error: {resp.status_code} {resp.text}")
    return resp.json() 