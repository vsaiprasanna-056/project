from sqlalchemy.orm import Session
import models
import schemas
import bcrypt
from fastapi import Response

from datetime import datetime, timedelta
import jwt
from sqlalchemy.exc import SQLAlchemyError

SECRET_KEY = "abcdefghijklmnopqrstuvwxyz"
ALGORITHM = "HS256"


def create_products(db: Session, products: schemas.productsCreate):
    #creating  a products object with user values
    db_products = models.products(**products.model_dump())
    #adding new products to existing table
    db.add(db_products)
    #commiting the changes to the database
    db.commit()
    #refreshing the database to get updated values
    db.refresh(db_products)
    #returning response to the user
    return db_products

def get_all_products(db: Session):
    return db.query(models.products).all()

def get_products(db: Session, products_id: int):
    return db.query(models.products).filter(
        models.products.id == products_id
    ).first()

def update_products(db: Session, products_id: int, products: schemas.productsCreate):
    db_products = get_products(db, products_id)
    if not db_products:
        return None
    db_products.productname = products.productname
    db_products.price=products.price 
    db_products.category=products.category
    db_products.colour=products.colour

    db.commit()
    db.refresh(db_products)
    return db_products

def delete_products(db: Session, products_id: int):
    db_products = get_products(db, products_id)
    if not db_products:
        return None
    db.delete(db_products)
    db.commit()
    return db_products



def get_prod_by_cate(db:Session,cate:str):
    print(cate)
    return db.query(models.products).filter(
        models.products.category==cate
    ).all()

    


def create_customer(customer: schemas.CustomerCreate, db: Session):
    try:
        new_customer = models.Customer(**customer.model_dump())

        hashed = bcrypt.hashpw(
            new_customer.password.encode(),
            bcrypt.gensalt(rounds=12)
        ).decode("utf-8")

        new_customer.password = hashed

        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)

        return new_customer

    except Exception as e:
        db.rollback()
        print("ERROR:", e)
        raise

def login_customer(customer: schemas.CustomerLogin,
                   db: Session,
                   response: Response):

    is_exists = db.query(models.Customer).filter(
        models.Customer.email == customer.email
    ).first()

    if not is_exists:
        return {"message": "Customer not found"}

    valid = bcrypt.checkpw(
        customer.password.encode(),
        is_exists.password.encode()
    )

    if not valid:
        return {"message": "Invalid password"}

    payload = {
        "customer_name": is_exists.customer_name,
        "email": is_exists.email,
        "is_admin": is_exists.is_admin,
        "is_loggedin": True,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True
    )

    return {
        "message": "Login successful",
        "access_token": token
    }
