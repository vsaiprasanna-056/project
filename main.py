from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






@app.post("/products", response_model=schemas.productsResponse)
def create(products: schemas.productsCreate, db: Session = Depends(get_db)):
    return crud.create_products(db, products)

@app.get("/products", response_model=list[schemas.productsResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all_products(db)

@app.get("/products/{products_id}", response_model=schemas.productsResponse)
def read_one(products_id: int, db: Session = Depends(get_db)):
    products = crud.get_products(db, products_id)
    if not products:
        raise HTTPException(status_code=404, detail="products not found")
    return products

@app.put("/products/{products_id}", response_model=schemas.productsResponse)
def update(products_id: int, products: schemas.productsCreate, db: Session = Depends(get_db)):
    updated = crud.update_products(db, products_id, products)
    if not updated:
        raise HTTPException(status_code=404, detail="products not found")
    return updated

@app.delete("/products/{products_id}")
def delete(products_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_products(db, products_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="products not found")
    return {"message":"products deleted successfully"}




@app.get("/cate/{cate}")
def get_cate_prod(cate:str,db:Session=Depends(get_db)):
    return crud.get_prod_by_cate(db,cate)
