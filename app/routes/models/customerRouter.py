from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db

import schemas
import services.customer as service

router = APIRouter(tags=["Customers"])


@router.post("/customer", response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return service.create_customer(db, customer)


@router.get("/customers", response_model=List[schemas.CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return service.get_customers(db)


@router.get("/customer/{customer_id}", response_model=schemas.CustomerResponse)
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    return service.get_customer_by_id(db, customer_id)


@router.put("/customer/{customer_id}", response_model=schemas.CustomerResponse)
def update_customer(customer_id: str, customer: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    return service.update_customer(db, customer_id, customer)


@router.delete("/customer/{customer_id}")
def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    return service.delete_customer(db, customer_id)
