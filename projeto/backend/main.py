from fastapi import Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from projeto.backend.routers import routers
from backend.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import User
from backend.auth import hash_password
from backend.schemas import UserCreate
from fastapi.responses import HTMLResponse
from backend.schemas import UserLogin
from backend.auth import verify_password, create_access_token
import json
from passlib.context import CryptContext
from backend.schemas import Review
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()
app.include_router(routers.router)
Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

app.add_middleware(
 CORSMiddleware,
    allow_origins=["*"],  # Lista de domínios permitidos
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["Access-Control-Allow-Origin", "Access-Control-Allow-Methods", "Access-Control-Allow-Headers"],  # Cabeçalhos permitidos
)

app.mount("/static", StaticFiles(directory=os.path.dirname(__file__)), name="static")

def load_reviews(filename):
    path = Path(filename)
    if path.is_file():
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_reviews(filename, reviews):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(reviews, file, indent=4)


@app.get("/home")
async def get_homepage():
    file_path = os.path.join(os.path.dirname(__file__), "home.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        return HTMLResponse(content="<h1>Página não encontrada</h1>", status_code=404)

@app.delete("/reviews/boca/{review_index}")
async def delete_review_boca(review_index: int):
    filename = 'reviews_boca.json'
    reviews = load_reviews(filename)
    if 0 <= review_index < len(reviews):
        deleted_review = reviews.pop(review_index)
        save_reviews(filename, reviews)
        return {"message": "Review excluído com sucesso", "review": deleted_review}
    else:
        raise HTTPException(status_code=404, detail="Review não encontrado")

@app.delete("/reviews/olhos/{review_index}")
async def delete_review_olhos(review_index: int):
    filename = 'reviews_olhos.json'
    reviews = load_reviews(filename)
    if 0 <= review_index < len(reviews):
        deleted_review = reviews.pop(review_index)
        save_reviews(filename, reviews)
        return {"message": "Review excluído com sucesso", "review": deleted_review}
    else:
        raise HTTPException(status_code=404, detail="Review não encontrado")
    
@app.delete("/reviews/rosto/{review_index}")
async def delete_review_rosto(review_index: int):
    filename = 'reviews_rosto.json'
    reviews = load_reviews(filename)
    if 0 <= review_index < len(reviews):
        deleted_review = reviews.pop(review_index)
        save_reviews(filename, reviews)
        return {"message": "Review excluído com sucesso", "review": deleted_review}
    else:
        raise HTTPException(status_code=404, detail="Review não encontrado")
    
@app.get("/rosto")
async def get_rosto_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "rosto.html"))

@app.post("/reviews/rosto")
async def add_review_rosto(review: Review):
    filename = 'reviews_rosto.json'
    reviews = load_reviews(filename)
    reviews.append(review.dict())
    save_reviews(filename, reviews)
    return {"message": "Review de rosto adicionado com sucesso!"}

@app.post("/reviews/olhos")
async def add_review_olhos(review: Review):
    filename = 'reviews_olhos.json'
    reviews = load_reviews(filename)
    reviews.append(review.dict())
    save_reviews(filename, reviews)
    return {"message": "Review de olhos adicionado com sucesso!"}

@app.post("/reviews/boca")
async def add_review_boca(review: Review):
    filename = 'reviews_boca.json'
    reviews = load_reviews(filename)
    reviews.append(review.dict())
    save_reviews(filename, reviews)
    return {"message": "Review de boca adicionado com sucesso!"}

@app.get("/reviews/rosto")
async def get_reviews_rosto():
    filename = 'reviews_rosto.json'
    return load_reviews(filename)

@app.get("/reviews/olhos")
async def get_reviews_olhos():
    filename = 'reviews_olhos.json'
    return load_reviews(filename)


@app.get("/reviews/boca")
async def get_reviews_boca():
    filename = 'reviews_boca.json'
    return load_reviews(filename)

@app.get("/olhos")
async def get_olhos_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "olhos.html"))

@app.get("/boca")
async def get_boca_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "boca.html"))

@app.get("/", response_class=HTMLResponse)
async def get_index():
    
    login_file_path = os.path.join(os.path.dirname(__file__), "index.html")
    
    try:
        
        with open(login_file_path, "r") as file:
            content = file.read()
        return HTMLResponse(content=content)
    except FileNotFoundError:
        return HTMLResponse("Arquivo 'index.html' não encontrado.", status_code=404)
    
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

@app.post("/login")
async def login(request: Request, user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    body = await request.body()  # Log do corpo da solicitação
    print("Corpo da solicitação recebido (bruto):", body)

    try:
        print("Dados recebidos (decodificados):", user.dict())
    except Exception as e:
        print("Erro ao decodificar dados:", e)
        raise HTTPException(status_code=422, detail=f"Erro ao decodificar a solicitação: {str(e)}")

    # Criação do token de acesso
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/forgot-password")
async def get_forgot_password_page():
    return FileResponse(os.path.join(os.path.dirname(__file__), "forgot-password.html"))