from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..config.db import get_db
from .. import crud

router = APIRouter()

@router.get("/products/", response_model=list[schemas.ProductBase])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@router.get("/product/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="product not found")
    return db_product

@router.get("/products_max/{max_price}")
def get_products_under(max_price: int = 0, db: Session = Depends(get_db)):
    products = crud.get_products_max(db, max_price = max_price)
    return products

@router.get("/products_min/{min_price}")
def get_products_above(min_price: int = 0, db: Session = Depends(get_db)):
    products = crud.get_products_min(db, min_price = min_price)
    return products

@router.get("/products_between/")
def get_products_between(min_price: int = 0, max_price: int = 0, db: Session = Depends(get_db)):
    products = crud.get_products_between(db, min_price = min_price, max_price = max_price)
    return products


@router.post("/products/")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@router.delete("/product/{product_id}", response_model=bool)
def delete_product(product_id: int,db: Session = Depends(get_db)):
    deleted = crud.delete_product_by_id(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return True

@router.put("/product/{product_id}")
def update_product(product: schemas.ProductUpdate, product_id: int, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)