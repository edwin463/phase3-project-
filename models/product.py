from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False, default=0)
    
    # Relationship: One product can have many sales
    sales = relationship("Sale", back_populates="product", cascade="all, delete-orphan")
    
    def __init__(self, name, category, price, stock_quantity):
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
    
    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, category={self.category}, price={self.price}, stock={self.stock_quantity})>"
    
    def update_stock(self, quantity):
        """ Update stock quantity when items are sold or restocked."""
        if self.stock_quantity + quantity < 0:
            raise ValueError("Not enough stock available!")
        self.stock_quantity += quantity