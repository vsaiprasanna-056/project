from pydantic import BaseModel
class productsCreate(BaseModel):
    productname: str
    price:int 
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
    is_admin: bool = False


class CustomerResponse(CustomerCreate):
    id: int

    model_config = {
        "from_attributes": True
    }


class CustomerLogin(BaseModel):
    email: str
    password: str
