from fastapi import FastAPI
from .database import engine, Base
from .routers import routers, routers_review
from fastapi.responses import HTMLResponse

# Inicialize o banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclua os roteadores
app.include_router(routers.router, prefix="/users", tags=["users"])
app.include_router(routers_review.router, prefix="/reviews", tags=["reviews"])
