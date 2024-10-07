from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class OrderBase(BaseModel):
    customer_id: UUID
    status: str


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    status: Optional[str]
    payment_status: Optional[str]
    total_amount: Optional[float]


class OrderResponse(OrderBase):
    id: UUID
    order_date: str

    class Config:
        from_attributes = True
