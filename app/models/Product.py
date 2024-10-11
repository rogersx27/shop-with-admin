from datetime import datetime
from re import T
from sqlalchemy import Column, DateTime, String, DECIMAL, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import uuid


class Product(Base):
    __tablename__ = "products"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True
    )

    generic_name = Column(String(255), nullable=False, unique=True)
    category_id = Column(String(36), ForeignKey("categories.id"), nullable=False)
    description = Column(Text)
    image_url = Column(String(255))
    availability = Column(Boolean, default=True)
    is_best_seller = Column(Boolean, default=False)
    large_description = Column(Text, nullable=True)
    brand_name = Column(String(255), nullable=False)
    manufacturer = Column(String(255), nullable=False)
    composition = Column(Text)
    supply_type = Column(String(50), nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    category = relationship("Category", back_populates="products")
    product_details = relationship("ProductDetail", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")
