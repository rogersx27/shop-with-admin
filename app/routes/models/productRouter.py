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


@router.get("/products/best-sellers/field/", response_model=List[schemas.ProductResponse])
def get_best_sellers_by_field(db: Session = Depends(get_db)):
    return service.get_best_sellers_by_field(db=db)


@router.get("/products/best-sellers/sales/", response_model=List[schemas.ProductResponse], )
def get_best_sellers_by_sales(db: Session = Depends(get_db)):
    return service.get_best_sellers_by_sales(db=db)


@router.get("/products/{num_products}/", response_model=List[schemas.ProductResponse])
def get_some_products(num_products: int = 5, db: Session = Depends(get_db)):
    return service.get_random_products(db=db, num_products=num_products)
