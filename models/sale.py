from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base, session
from models.product import Product

class Sale(Base):
    __tablename__ = 'sales'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    
    # Relationship: Each sale is linked to one product
    product = relationship("Product", back_populates="sales")
    
    def __init__(self, product_id, quantity_sold, total_price):
        self.product_id = product_id
        self.quantity_sold = quantity_sold
        self.total_price = total_price
    
    def __repr__(self):
        return f"<Sale(id={self.id}, product_id={self.product_id}, quantity={self.quantity_sold}, total_price={self.total_price})>"
    
    @classmethod
    def record_sale(cls, product_id, quantity_sold):
        """ Record a sale and update product stock. """
        product = session.query(Product).filter_by(id=product_id).first()
        if not product:
            raise ValueError("Product not found!")
        if product.stock_quantity < quantity_sold:
            raise ValueError("Insufficient stock!")
        
        total_price = quantity_sold * product.price
        new_sale = cls(product_id=product_id, quantity_sold=quantity_sold, total_price=total_price)
        
        product.update_stock(-quantity_sold)  # Deduct stock
        session.add(new_sale)
        session.commit()
        return new_sale
