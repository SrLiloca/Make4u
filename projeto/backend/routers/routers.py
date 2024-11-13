from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import models, schemas
from backend.database import get_db
from backend.auth import get_password_hash, create_user

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

@router.post("/signup", response_model=schemas.UserResponse)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verificando se o email já está registrado
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    # Criando o usuário com senha hashada
    return create_user(db=db, user=user)

