from sqlalchemy import Column, Integer, String
from database import Base

class products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    productname = Column(String(100), nullable=False)
    price = Column(String(100), nullable=False)
    category= Column(String(50),nullable=False)
    colour=Column(String(70),nullable=True)
    