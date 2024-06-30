from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models
from ..config.db import get_db
from .. import crud

router = APIRouter()

@router.get("/ratings")
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_ratings(db, skip=skip, limit=limit)

@router.get("/rating/{rating_id}")
def get_rating(rating_id: int, db: Session = Depends(get_db)):
    db_rating = crud.get_rating(db, rating_id=rating_id)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="rating not found")
    return db_rating

@router.get("/ratings_product/{product_id}")
def get_ratings_from_product(product_id: int, db: Session = Depends(get_db)):
    db_rating = crud.get_ratings_from_product(db, product_id=product_id)
    if db_rating is None:
        raise HTTPException(status_code=404, detail="rating not found")
    return db_rating

@router.post("/ratings/")
def create_rating(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    return crud.create_rating(db=db, rating=rating)

@router.delete("/rating/{rating_id}", response_model=bool)
def delete_rating(rating_id: int,db: Session = Depends(get_db)):
    deleted = crud.delete_rating_by_id(db, rating_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Rating not found")
    return True
