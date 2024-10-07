from sqlalchemy.orm import Session
import schemas
import models

from .general import create_instance, delete_instance, get_all_instances, get_instance_by_id, update_instance

def create_customer(db: Session, customer: schemas.CustomerCreate):
    return create_instance(db, models.Customer, customer)


def get_customers(db: Session):
    return get_all_instances(db, models.Customer)


def get_customer_by_id(db: Session, customer_id: str):
    return get_instance_by_id(db, models.Customer, customer_id)


def update_customer(db: Session, customer_id: str, customer_update: schemas.CustomerUpdate):
    return update_instance(db, models.Customer, customer_id, customer_update)


def delete_customer(db: Session, customer_id: str):
    return delete_instance(db, models.Customer, customer_id)
