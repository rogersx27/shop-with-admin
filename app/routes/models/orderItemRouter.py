from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db

import schemas
import services.orderItem as service


router = APIRouter(tags=["Orders Items"])


@router.post("/orderItems/", response_model=schemas.OrderItemResponse)
def create_orderItem(orderItem: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return service.create_orderItem(db=db, orderItem=orderItem)


@router.get("/orderItems/", response_model=List[schemas.OrderItemResponse])
def get_orderItems(db: Session = Depends(get_db)):
    return service.get_orderItems(db=db)


@router.get("/orderItems/{orderItem_id}/", response_model=schemas.OrderItemResponse)
def get_orderItem(orderItem_id: str, db: Session = Depends(get_db)):
    return service.get_orderItem_by_id(db=db, orderItem_id=orderItem_id)


@router.put("/orderItems/{orderItem_id}/", response_model=schemas.OrderItemResponse)
def update_orderItem(orderItem_id: str, orderItem: schemas.OrderItemUpdate, db: Session = Depends(get_db)):
    return service.update_orderItem(db=db, orderItem_id=orderItem_id, orderItem_update=orderItem)


@router.delete("/orderItems/{orderItem_id}/")
def delete_orderItem(orderItem_id: str, db: Session = Depends(get_db)):
    return service.delete_orderItem(db=db, orderItem_id=orderItem_id)
