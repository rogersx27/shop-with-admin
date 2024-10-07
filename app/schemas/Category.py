from pydantic import BaseModel
from uuid import UUID

from .Product import ProductLiteResponse


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: str


class CategoryResponse(CategoryBase):
    id: UUID

    class Config:
        from_attributes = True


class CategoryWithProductsResponse(BaseModel):
    id: UUID
    name: str
    products: list[ProductLiteResponse]

    class Config:
        from_attributes = True
