from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection
DATABASE_URL = "sqlite:///inventory.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Base class for models
Base = declarative_base()

# Function to initialize the database
def initialize_db():
    from models.product import Product
    from models.sale import Sale
    from models.expense import Expense
    
    Base.metadata.create_all(engine)
    print("Database initialized successfully!")
