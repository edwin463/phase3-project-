from sqlalchemy import Column, Integer, String, Float, DateTime
from database.connection import Base, session
from datetime import datetime

class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)
    
    def __init__(self, category, amount, description=None):
        self.category = category
        self.amount = amount
        self.description = description
    
    def __repr__(self):
        return f"<Expense(id={self.id}, category={self.category}, amount={self.amount}, date={self.date})>"
    
    @classmethod
    def add_expense(cls, category, amount, description=None):
        """ Adds a new expense record to the database. """
        new_expense = cls(category=category, amount=amount, description=description)
        session.add(new_expense)
        session.commit()
        return new_expense
