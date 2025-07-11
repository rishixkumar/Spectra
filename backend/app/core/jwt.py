"""
jwt.py

This module provides JWT (JSON Web Token) utility functions for authentication in the FastAPI application.
It loads the secret key, algorithm, and token expiry from environment variables (using python-dotenv to load from a .env file).

- SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES are loaded from .env
- create_access_token: Generates a JWT access token for a given payload and expiry
"""
import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
#------------------------------------------------------------------------

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key")  # Replace with a secure key in production!
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 60))

#------------------------------------------------------------------------
def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Create a JWT access token.

    Args:
        data (dict): The payload to encode in the token.
        expires_delta (timedelta, optional): Expiry duration. Defaults to ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns:
        str: Encoded JWT token as a string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt 