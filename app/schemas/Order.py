from pydantic import BaseModel
from uuid import UUID


class OrderBase(BaseModel):
    customer_id: UUID
    status: str


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: UUID
    order_date: str

    class Config:
        from_attributes = True


class OrderItemBase(BaseModel):
    order_id: UUID
    product_id: UUID
    quantity: int
    price: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: UUID

    class Config:
        from_attributes = True
