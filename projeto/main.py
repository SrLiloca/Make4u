from fastapi import FastAPI
from .database import engine, Base
from .routers import routers, routers_review
from fastapi.responses import FileResponse
from starlette.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

# Inicialize o banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclua os roteadores
app.include_router(routers.router, prefix="/users", tags=["users"])
app.include_router(routers_review.router, prefix="/reviews", tags=["reviews"])

app.mount("/static", StaticFiles(directory=r"C:\Users\thali\make\static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

class Review(BaseModel):
    product_name: str
    brand: str
    rating: int
    review_text: str
    image_url: str

@app.get("/category/{category}", response_class=HTMLResponse)
async def category_page(category: str):
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Categoria {category}</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Bem-vindo à categoria: {category}</h1>
        <!-- Lista de subcategorias aqui -->
    </body>
    </html>
    """)

@app.post("/api/reviews")
async def add_review(review: Review):
    # Aqui você pode processar os dados e salvar em um banco de dados, por exemplo
    print(review)
    return {"message": "Resenha adicionada com sucesso!"}