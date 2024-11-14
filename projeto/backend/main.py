from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from backend.routers import routers
from backend.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User
from backend.auth import hash_password
from backend.schemas import UserCreate
from fastapi.responses import HTMLResponse

app = FastAPI()
app.include_router(routers.router)

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

@app.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Verifique se o e-mail já existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário com este e-mail já está registrado."
        )
    
    # Criptografa a senha do usuário
    hashed_password = hash_password(user.password)
    
    # Cria um novo usuário
    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        is_active=True  # Ajuste conforme necessário
    )
    
    # Adiciona e confirma a inserção no banco de dados
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"success": True, "message": "Usuário cadastrado com sucesso!"}