from sqlalchemy.orm import Session
import models
import schemas

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

    
