from sqlalchemy.orm import Session
import schemas
import models

from .general import create_instance, delete_instance, get_all_instances, get_instance_by_id, update_instance


def create_product(db: Session, product: schemas.ProductCreate):
    return create_instance(db, models.Product, product)


def get_products(db: Session):
    return get_all_instances(db, models.Product)


def get_product_by_id(db: Session, product_id: str):
    return get_instance_by_id(db, models.Product, product_id)


def update_product(db: Session, product_id: str, product_update: schemas.ProductUpdate):
    return update_instance(db, models.Product, product_id, product_update)


def delete_product(db: Session, product_id: str):
    return delete_instance(db, models.Product, product_id)
