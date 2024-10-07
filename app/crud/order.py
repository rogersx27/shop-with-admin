from sqlalchemy.orm import Session
import schemas
import models

from .general import create_instance, delete_instance, get_all_instances, get_instance_by_id, update_instance

def create_order(db: Session, order: schemas.OrderCreate):
    return create_instance(db, models.Order, order)


def get_orders(db: Session):
    return get_all_instances(db, models.Order)


def get_order_by_id(db: Session, order_id: str):
    return get_instance_by_id(db, models.Order, order_id)


def update_order(db: Session, order_id: str, order_update: schemas.OrderUpdate):
    return update_instance(db, models.Order, order_id, order_update)


def delete_order(db: Session, order_id: str):
    return delete_instance(db, models.Order, order_id)
