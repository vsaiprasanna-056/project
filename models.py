from sqlalchemy import Column, Integer, String
from database import Base

class products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    productname = Column(String(100), nullable=False)
    price = Column(String(100), nullable=False)
    category= Column(String(50),nullable=False)
    colour=Column(String(70),nullable=True)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), unique=True, nullable=False)
    address = Column(String(255), nullable=False)
    password = Column(String(300), nullable=False)    