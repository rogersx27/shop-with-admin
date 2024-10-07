from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base
import uuid


class Order(Base):
    __tablename__ = 'orders'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    customer_id = Column(String(36), ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.now, nullable=False)
    status = Column(String(50), nullable=False)
    total_amount = Column(DECIMAL(10, 2), default=0, nullable=False)
    payment_status = Column(String(50))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    order_id = Column(String(36), ForeignKey('orders.id'), nullable=False)
    product_id = Column(String(36), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")
