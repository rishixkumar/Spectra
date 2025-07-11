"""
main.py

This is the entry point for the FastAPI application.

- Initializes the FastAPI app instance.
- Defines the root endpoint ("/") for a basic health check or welcome message.
- Includes the user router for user-related API endpoints (registration, login, etc.).
- Runs database initialization on application startup to ensure all tables are created.
"""
from fastapi import FastAPI
from app.routers import user
from app.core.init_db import init_db
#------------------------------------------------------------------------

app = FastAPI()

#------------------------------------------------------------------------
@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    Returns:
        dict: A welcome message.
    """
    return {"message": "Hello World"}

app.include_router(user.router) 

#------------------------------------------------------------------------
@app.on_event("startup")
def on_startup():
    """
    FastAPI startup event handler.
    Initializes the database tables at application startup.
    """
    init_db()