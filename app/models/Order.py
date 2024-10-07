from sqlalchemy import Column, String, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base
import uuid


class Order(Base):
    __tablename__ = 'orders'

    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    customer_id = Column(String(36), ForeignKey('customers.id'), nullable=False)
    order_date = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)

    customer = relationship("Customer")


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    order_id = Column(String(36), ForeignKey('orders.id'), nullable=False)
    product_id = Column(String(36), ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order")
    product = relationship("Product")
