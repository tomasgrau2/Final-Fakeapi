from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from sqlalchemy import update
from .models import Product, Rating
from . import  schemas

#PRODUCT

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_id: int):
    return (db.query(Product).filter(Product.id == product_id).first())


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, updated_product):
    db.query(Product).filter(Product.id == product_id).update(dict(updated_product))
    db.commit()

def delete_product_by_id(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    # Si se encontró el producto, elimínalo
    if product:
        db.delete(product)
        db.commit()
        return True  # Indica que se eliminó con éxito
    else:
        return False

def get_products_between(db: Session, min_price: int = 0, max_price: int = 0):
    return db.query(Product).filter((Product.precio_compra > min_price) & (Product.precio_compra < max_price)).all()

def get_products_min(db: Session, min_price: int = 0):
    return db.query(Product).filter(Product.precio_compra > min_price).all()

def get_products_max(db: Session, max_price: int = 0):
    return db.query(Product).filter(Product.precio_compra < max_price).all()


# RATING


def get_ratings_from_product(db: Session, product_id: int):
    return db.query(Rating).filter(Rating.product_id == product_id).all()

def get_ratings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Rating).offset(skip).limit(limit).all()

def get_rating(db: Session, rating_id: int):
    return (db.query(Rating).filter(Rating.id == rating_id).first())

def create_rating(db: Session, rating: schemas.RatingCreate):
    db_rating = Rating(**rating.model_dump())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def delete_rating_by_id(db: Session, rating_id: int):
    rating = db.query(Rating).filter(Rating.id == rating_id).first()
    # Si se encontró el ratingo, elimínalo
    if rating:
        db.delete(rating)
        db.commit()
        return True  # Indica que se eliminó con éxito
    else:
        return False