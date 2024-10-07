from typing import List
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base
import uuid


class Category(Base):
    __tablename__ = 'categories'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    products = relationship("Product", back_populates="category")
