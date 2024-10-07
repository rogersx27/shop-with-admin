from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db

import schemas
import services.productDetail as service


router = APIRouter(tags=["Product Details"])


@router.post("/productDetails/", response_model=schemas.ProductDetailResponse)
def create_productDetail(productDetail: schemas.ProductDetailCreate, db: Session = Depends(get_db)):
    return service.create_productDetail(db=db, productDetail=productDetail)


@router.get("/productDetails/", response_model=List[schemas.ProductDetailResponse])
def get_productDetails(db: Session = Depends(get_db)):
    return service.get_productDetails(db=db)


@router.get("/productDetails/{productDetail_id}/", response_model=schemas.ProductDetailResponse)
def get_productDetail(productDetail_id: str, db: Session = Depends(get_db)):
    return service.get_productDetail_by_id(db=db, productDetail_id=productDetail_id)


@router.put("/productDetails/{productDetail_id}/", response_model=schemas.ProductDetailResponse)
def update_productDetail(productDetail_id: str, productDetail: schemas.ProductDetailUpdate, db: Session = Depends(get_db)):
    return service.update_productDetail(db=db, productDetail_id=productDetail_id, productDetail_update=productDetail)


@router.delete("/productDetails/{productDetail_id}/")
def delete_productDetail(productDetail_id: str, db: Session = Depends(get_db)):
    return service.delete_productDetail(db=db, productDetail_id=productDetail_id)
