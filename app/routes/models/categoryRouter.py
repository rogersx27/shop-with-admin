from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db

import schemas
import services.category as service

router = APIRouter(tags=["Categories"])


@router.post("/categories/", response_model=schemas.CategoryResponse)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return service.create_category(db=db, category=category)


@router.get("/categories/", response_model=List[schemas.CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return service.get_categories(db=db)


@router.get("/categories/{category_id}/", response_model=schemas.CategoryResponse)
def get_category(category_id: str, db: Session = Depends(get_db)):
    return service.get_category_by_id(db=db, category_id=category_id)


@router.put("/categories/{category_id}/", response_model=schemas.CategoryResponse)
def update_category(category_id: str, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    return service.update_category(db=db, category_id=category_id, category_update=category)


@router.delete("/categories/{category_id}/")
def delete_category(category_id: str, db: Session = Depends(get_db)):
    return service.delete_category(db=db, category_id=category_id)
