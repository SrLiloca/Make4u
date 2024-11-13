from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
<<<<<<< HEAD
from backend.database import Base
from pydantic import BaseModel
from backend.schemas import UserCreate
=======
from .database import Base
from pydantic import BaseModel
>>>>>>> 85ac6157ab1e23eba03221561352181474c3f6f1

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    brand = Column(String)
    category = Column(String)
    subcategory = Column(String)
    rating = Column(Integer)
    text = Column(String(280))
    image_url = Column(String, nullable=True)
    
    # Relacionamento com a tabela User (garantindo que 'owner' exista na tabela User)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="reviews")  # Relacionamento com a tabela User

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  # Adicionei o campo 'name' aqui
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    reviews = relationship("Review", back_populates="user")
<<<<<<< HEAD
=======

class UserCreate(BaseModel):
    name: str  # Adicionei o campo 'name' aqui
    email: str
    password: str
>>>>>>> 85ac6157ab1e23eba03221561352181474c3f6f1
