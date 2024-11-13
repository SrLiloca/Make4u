from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from backend.routers import routers
from backend.database import engine, Base
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
 CORSMiddleware,
    allow_origins=["*"],  # Lista de domínios permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["Access-Control-Allow-Origin", "Access-Control-Allow-Methods", "Access-Control-Allow-Headers"],  # Cabeçalhos permitidos
)

Base.metadata.create_all(bind=engine)
app.include_router(routers.router, prefix="/users", tags=["users"])


app.mount("/static", StaticFiles(directory=os.path.dirname(__file__)), name="static")

@app.get("/")
async def get_homepage():
    return FileResponse(os.path.join(os.path.dirname(__file__), "login.html"))

@app.get("/forgot-password")
async def get_forgot_password_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "forgot-password.html"))


@app.get("/reviews")
async def get_reviews_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "reviews.html"))

@app.get("/login", response_class=HTMLResponse)
async def get_login():
    
    login_file_path = os.path.join(os.path.dirname(__file__), "login.html")
    
    try:
        
        with open(login_file_path, "r") as file:
            content = file.read()
        return HTMLResponse(content=content)
    except FileNotFoundError:
        return HTMLResponse("Arquivo 'login.html' não encontrado.", status_code=404)
    
@app.get("/signup", response_class=HTMLResponse)
async def get_signup_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "signup.html"))