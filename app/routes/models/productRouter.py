from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db

import schemas
import services.product as service


router = APIRouter(tags=["Products"])


@router.post("/products/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return service.create_product(db=db, product=product)


@router.get("/products/", response_model=List[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return service.get_products(db=db)


@router.get("/products/{product_id}/", response_model=schemas.ProductResponse)
def get_product(product_id: str, db: Session = Depends(get_db)):
    return service.get_product_by_id(db=db, product_id=product_id)


@router.put("/products/{product_id}/", response_model=schemas.ProductResponse)
def update_product(product_id: str, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    return service.update_product(db=db, product_id=product_id, product_update=product)


@router.delete("/products/{product_id}/")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    return service.delete_product(db=db, product_id=product_id)
