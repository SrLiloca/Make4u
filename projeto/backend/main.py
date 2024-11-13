from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from backend.routers import routers
from backend.database import engine, Base
from fastapi.responses import HTMLResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(routers.router, prefix="/users", tags=["users"])

# Configura o diretório estático para procurar arquivos dentro da própria pasta 'backend'
app.mount("/static", StaticFiles(directory=os.path.dirname(__file__)), name="static")

# Rota para a página inicial
@app.get("/")
async def get_homepage():
    return FileResponse(os.path.join(os.path.dirname(__file__), "login.html"))

# Exemplo de rota para servir a página de signup
@app.get("/signup")
async def get_signup_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "signup.html"))

# Exemplo de rota para servir a página de recuperação de senha
@app.get("/forgot-password")
async def get_forgot_password_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "forgot-password.html"))

# Exemplo de rota para servir a página de reviews
@app.get("/reviews")
async def get_reviews_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "reviews.html"))

@app.get("/signup")
async def signup():
    return FileResponse("signup.html")

@app.get("/login", response_class=HTMLResponse)
async def get_login():
    # Definindo o caminho do arquivo 'login.html' na mesma pasta que o main.py
    login_file_path = os.path.join(os.path.dirname(__file__), "login.html")
    
    try:
        # Abrindo o arquivo 'login.html'
        with open(login_file_path, "r") as file:
            content = file.read()
        return HTMLResponse(content=content)
    except FileNotFoundError:
        return HTMLResponse("Arquivo 'login.html' não encontrado.", status_code=404)