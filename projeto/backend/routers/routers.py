from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas, auth
from backend.database import get_db
from backend.schemas import UserCreate

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Criptografar a senha
        hashed_password = hash_password(user.password)

        # Criar um novo usuário
        db_user = models.User(name=user.name, email=user.email, hashed_password=hashed_password)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"success": True, "message": "Usuário cadastrado com sucesso!"}
    
    except Exception as e:
        # Exibe o erro detalhado no log do servidor
        print(f"Erro ao cadastrar usuário: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {e}")
    finally:
        db.close()