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