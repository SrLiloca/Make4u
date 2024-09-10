from fastapi import FastAPI
from routers import search
from database import init_db

app = FastAPI()

init_db()

app.include_router(search.router, prefix="/products")
