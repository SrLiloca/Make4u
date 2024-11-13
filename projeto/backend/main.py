from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

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

