from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, DECIMAL, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import uuid

class ProductDetail(Base):
    __tablename__ = 'product_details'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    product_id = Column(String(36), ForeignKey('products.id'), nullable=False)
    brand_name = Column(String(255), nullable=False)
    strength = Column(String(50), nullable=False)
    composition = Column(Text)
    supply_type = Column(String(50), nullable=False)
    manufacturer = Column(String(255), nullable=False)
    other_brand_names = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="product_details")