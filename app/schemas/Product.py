from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class ProductBase(BaseModel):
    generic_name: str
    category_id: UUID
    description: Optional[str] = None
    image_url: Optional[str] = None
    availability: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    generic_name: Optional[str]
    category_id: Optional[UUID]
    description: Optional[str]
    image_url: Optional[str]
    availability: Optional[bool]


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
