from pydantic import BaseModel
from typing import Optional

from uuid import UUID


class ProductDetailBase(BaseModel):
    product_id: UUID
    brand_name: Optional[str]
    strength: Optional[str]
    composition: Optional[str]
    supply_type: Optional[str]
    manufacturer: Optional[str]
    other_brand_names: Optional[str]
    price: Optional[float]
    stock: Optional[int]


class ProductDetailCreate(ProductDetailBase):
    pass


class ProductDetailUpdate(BaseModel):
    brand_name: Optional[str]
    strength: Optional[str]
    composition: Optional[str]
    supply_type: Optional[str]
    manufacturer: Optional[str]
    other_brand_names: Optional[str]
    price: Optional[float]
    stock: Optional[int]


class ProductDetailResponse(ProductDetailBase):
    product_id: Optional[UUID]

    class Config:
        from_attributes = True
