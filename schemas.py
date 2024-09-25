from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    inventory_count: int
    category: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    popularity_score: float

    class Config:
        orm_mode = True
