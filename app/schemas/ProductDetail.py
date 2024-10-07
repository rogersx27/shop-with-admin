from pydantic import BaseModel
from typing import Optional

from uuid import UUID


class ProductDetailBase(BaseModel):
    product_id: UUID
    brand_name: str
    strength: str
    composition: str | None = None
    supply_type: str
    manufacturer: str
    other_brand_names: str | None = None
    price: float
    stock: int


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
    id: UUID

    class Config:
        from_attributes = True
