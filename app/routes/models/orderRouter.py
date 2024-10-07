from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db

import schemas
import services.order as service

router = APIRouter(tags=["Orders"])


@router.post("/orders/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return service.create_order(db=db, order=order)


@router.get("/orders/", response_model=List[schemas.OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return service.get_orders(db=db)


@router.get("/orders/{order_id}/", response_model=schemas.OrderResponse)
def get_order(order_id: str, db: Session = Depends(get_db)):
    return service.get_order_by_id(db=db, order_id=order_id)


@router.put("/orders/{order_id}/", response_model=schemas.OrderResponse)
def update_order(order_id: str, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    return service.update_order(db=db, order_id=order_id, order_update=order)


@router.delete("/orders/{order_id}/")
def delete_order(order_id: str, db: Session = Depends(get_db)):
    return service.delete_order(db=db, order_id=order_id)
