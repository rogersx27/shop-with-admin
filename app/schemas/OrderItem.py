from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class OrderItemBase(BaseModel):
    order_id: UUID
    product_id: UUID
    quantity: int
    price: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemUpdate(BaseModel):
    product_id: Optional[UUID]
    quantity: Optional[int]
    price: Optional[float]


class OrderItemResponse(OrderItemBase):
    id: UUID

    class Config:
        from_attributes = True
