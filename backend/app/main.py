"""
main.py

This is the entry point for the FastAPI application.

- Initializes the FastAPI app instance.
- Defines the root endpoint ("/") for a basic health check or welcome message.
- Includes all routers for user, watchlist, stock, news, historical, and admin endpoints.
- Runs database initialization on application startup to ensure all tables are created.
"""
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.routers import user
from app.routers import watchlist
from app.routers import stock
from app.routers import news
from app.routers import historical
from app.routers import admin
from app.core.init_db import init_db
#------------------------------------------------------------------------

app = FastAPI(
    title="Spectra",
    version="MVP 1.0.0",
    description="Spectra API for user authentication, watchlists, stock data, and news.",
    openapi_tags=[
        {"name": "User", "description": "User registration, login, profile, etc."},
        {"name": "Watchlist", "description": "User watchlist management."},
        {"name": "Stock", "description": "Stock summary and chart endpoints."},
        {"name": "Stock History", "description": "Historical OHLCV and stats endpoints."},
        {"name": "News", "description": "Stock and global news endpoints."},
        {"name": "Admin", "description": "Admin endpoints."}
    ]
)
#------------------------------------------------------------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

app.include_router(user.router)
app.include_router(watchlist.router)
app.include_router(stock.router)
app.include_router(news.router)
app.include_router(historical.router)
app.include_router(admin.router)
#------------------------------------------------------------------------

@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    Returns:
        dict: A welcome message.
    """
    return {"message": "Hello World"}
#------------------------------------------------------------------------
@app.on_event("startup")
def on_startup():
    """
    FastAPI startup event handler.
    Initializes the database tables at application startup.
    """
    init_db()