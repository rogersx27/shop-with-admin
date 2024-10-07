from sqlalchemy import Column, String, DECIMAL, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import uuid


class Product(Base):
    __tablename__ = 'products'

    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    category_id = Column(String(36), ForeignKey(
        'categories.id'), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text)
    image_url = Column(String(255))
    quantity = Column(String(50))
    availability = Column(Boolean, default=True)

    category = relationship("Category", back_populates="products")
