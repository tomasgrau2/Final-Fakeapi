from typing import List
from pydantic import BaseModel
from decimal import Decimal

# Esquema Pydantic para la clase Product
class ProductBase(BaseModel):
    titulo: str
    precio_compra: Decimal
    descripcion: str = None
    categoria: str = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    rating: List['Rating'] # Relación con la clase Rating

    class Config:
        orm_mode = True

# Esquema Pydantic para la clase Rating
class RatingBase(BaseModel):
    rate: Decimal

class RatingCreate(RatingBase):
    product_id: int

class RatingUpdate(RatingBase):
    pass

class Rating(RatingBase):
    product_id: int
    product: Product  # Relación con la clase Product

    class Config:
        orm_mode = True