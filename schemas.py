from pydantic import BaseModel
class productsCreate(BaseModel):
    productname: str
    price:str 
    category:str
    colour:str


class productsResponse(productsCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
class CustomerCreate(BaseModel):
    customer_name: str
    email: str
    phone: str
    address: str
    password: str


class CustomerResponse(CustomerCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


class CustomerLogin(BaseModel):
    email: str
    password: str