from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class ProductBase(BaseModel):
    name: str
    category_id: UUID
    price: float
    description: Optional[str] = None
    image_url: Optional[str] = None
    quantity: Optional[str] = None
    availability: bool = True


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: UUID

    class Config:
        from_attributes = True
        
class ProductLiteResponse(BaseModel):
    name: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    availability: bool = True
    price: float

    class Config:
        from_attributes = True
