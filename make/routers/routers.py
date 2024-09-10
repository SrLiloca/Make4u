from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from . import models
from models import Product, SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products/")
def search_products(
    query: str = Query(None),
    category: str = Query(None),
    subcategory: str = Query(None),
    sort_by: str = Query(None),
    db: Session = Depends(get_db)
):
    query_filters = []
    if query:
        query_filters.append(Product.name.ilike(f"%{query}%"))
    if category:
        query_filters.append(Product.category == category)
    if subcategory:
        query_filters.append(Product.subcategory == subcategory)

    products = db.query(Product).filter(*query_filters)

    if sort_by == "price_asc":
        products = products.order_by(Product.price)
    elif sort_by == "price_desc":
        products = products.order_by(Product.price.desc())
    else:
        products = products.order_by(Product.name)

    return products.all()

@app.post("/products/")
def create_product(product: models.Product, db: Session = Depends(get_db)):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

