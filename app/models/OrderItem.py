from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base
import uuid


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()), unique=True)
    order_id = Column(String(36), ForeignKey('orders.id'), nullable=False)
    product_id = Column(String(36), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")
