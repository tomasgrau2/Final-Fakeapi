from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from .config.db import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String,nullable=False)
    precio_compra = Column(Numeric(precision=10, scale=2),nullable=False)
    descripcion = Column(String)
    categoria = Column(String)

    rating = relationship('Rating', uselist=False, back_populates='product', cascade='all, delete-orphan')


class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, index=True)
    rate = Column(Numeric(precision=10, scale=2), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'))  
    
    product = relationship('Product', back_populates='rating')