from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class CustomerBase(BaseModel):
    name: str
    email: str
    address: Optional[str] = None
    phone: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    address: Optional[str]


class CustomerResponse(CustomerBase):
    id: UUID

    class Config:
        from_attributes = True
