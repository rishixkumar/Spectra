from fastapi import FastAPI
from app.routers import user
from app.core.init_db import init_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(user.router) 

@app.on_event("startup")
def on_startup():
    init_db()