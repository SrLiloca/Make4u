from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import models, schemas, auth
from backend.database import get_db
from backend.auth import hash_password
from pydantic import BaseModel
from backend import models, database
from backend.models import User
from backend.schemas import UserCreate

router = APIRouter()



@router.get("/reviews", response_model=list[schemas.ReviewResponse])
def get_reviews(category: str, db: Session = Depends(get_db)):
    return db.query(models.Review).filter(models.Review.category == category).all()

@router.post("/reviews", response_model=schemas.ReviewResponse)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    
    # Criar o token de acesso
    access_token = auth.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Verifique se o e-mail já existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário com este e-mail já está registrado."
        )

    # Criptografa a senha do usuário


    # Cria um novo usuário
    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
        is_active=True  # Ajuste conforme necessário
    )

    # Adiciona e confirma a inserção no banco de dados
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"success": True, "message": "Usuário cadastrado com sucesso!"}