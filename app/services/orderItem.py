from sqlalchemy.orm import Session
import schemas
import models

from .general import create_instance, delete_instance, get_all_instances, get_instance_by_id, update_instance

def create_orderItem(db: Session, orderItem: schemas.OrderItemCreate):
    return create_instance(db, models.OrderItem, orderItem)


def get_orderItems(db: Session):
    return get_all_instances(db, models.OrderItem)


def get_orderItem_by_id(db: Session, orderItem_id: str):
    return get_instance_by_id(db, models.OrderItem, orderItem_id)


def update_orderItem(db: Session, orderItem_id: str, orderItem_update: schemas.OrderItemUpdate):
    return update_instance(db, models.OrderItem, orderItem_id, orderItem_update)


def delete_orderItem(db: Session, orderItem_id: str):
    return delete_instance(db, models.OrderItem, orderItem_id)