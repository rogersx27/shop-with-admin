from pydantic import BaseModel
from typing import Dict, List, Optional

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


class ProductDetailBaseForAdmin(BaseModel):
    product_id: UUID
    strength: Optional[str]
    price: Optional[float]
    stock: Optional[int]
    packaging: Optional[str]
    quantity_per_pack: Optional[str]
    other_presentations: Optional[List[Dict[str, str]]]


class ProductDetailCreate(ProductDetailBaseForAdmin):
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
    product_id: UUID

    class Config:
        from_attributes = True
