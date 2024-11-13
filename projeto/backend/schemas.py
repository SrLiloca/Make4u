from pydantic import BaseModel, EmailStr
from typing import Optional

class ReviewBase(BaseModel):
    product_name: str
    brand: str
    category: str
    subcategory: str
    rating: int
    text: Optional[str] = None

class ReviewCreate(ReviewBase):
    pass

class ReviewResponse(ReviewBase):
    id: int
    user_id: int
    image_url: Optional[str] = None

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
<<<<<<< HEAD
    email: str

class UserCreate(BaseModel):
    name: str  
    email: str  
=======
    email: EmailStr

class UserCreate(BaseModel):
    name: str  
    email: EmailStr  
>>>>>>> 85ac6157ab1e23eba03221561352181474c3f6f1
    password: str  
class UserResponse(UserBase):
    id: int
    is_active: bool
    username: str
    email: str

    class Config:
        orm_mode = True
