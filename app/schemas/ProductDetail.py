from pydantic import BaseModel
from typing import Dict, List, Optional

from uuid import UUID


class ProductDetailBase(BaseModel):
    product_id: UUID
    strength: Optional[str]
    other_brand_names: Optional[str]
    other_presentations: Optional[List[Dict[str, str]]]


class ProductDetailBaseForAdmin(BaseModel):
    product_id: UUID
    strength: Optional[str]
    packaging: Optional[str]
    other_presentations: Optional[List[Dict[str, str]]]


class ProductDetailCreate(ProductDetailBaseForAdmin):
    pass


class ProductDetailUpdate(BaseModel):
    strength: Optional[str]
    other_brand_names: Optional[str]


class ProductDetailResponse(ProductDetailBase):
    product_id: UUID

    class Config:
        from_attributes = True
