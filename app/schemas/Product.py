from pydantic import BaseModel
from typing import Optional
from uuid import UUID

from schemas.ProductDetail import ProductDetailBase


class ProductBase(BaseModel):
    generic_name: str
    category_id: UUID
    description: Optional[str] = None
    image_url: Optional[str] = None
    availability: bool = True


class ProductBaseForAdmin(BaseModel):
    generic_name: str
    category_id: UUID
    description: Optional[str] = None
    image_url: Optional[str] = None
    availability: bool = True
    is_best_seller: bool = False
    large_description: Optional[str] = None

class ProductCreate(ProductBaseForAdmin):
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
    id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    category_name: Optional[str] = None
    generic_name: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    availability: bool = True

    details: Optional[ProductDetailBase]

    class Config:
        from_attributes = True
