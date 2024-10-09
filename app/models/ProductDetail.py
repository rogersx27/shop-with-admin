from sqlalchemy import JSON, Column, DateTime, Integer, String, DECIMAL, Boolean, Text, ForeignKey, null
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
    packaging = Column(String(255), nullable=True)
    quantity_per_pack = Column(String(255), nullable=True)
    other_presentations = Column(JSON, nullable=True)

    product = relationship("Product", back_populates="product_details")