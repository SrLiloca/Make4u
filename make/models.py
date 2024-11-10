from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from make.database import Base
from sqlalchemy import Boolean

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    brand = Column(String)
    category = Column(String)  # Ex: "pele", "olhos", "boca"
    subcategory = Column(String)  # Ex: "base", "batom"
    rating = Column(Integer)
    text = Column(String(280))
    image_url = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)