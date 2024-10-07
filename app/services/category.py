from sqlalchemy.orm import Session
import schemas
import models

from .general import create_instance, delete_instance, get_all_instances, get_instance_by_id, update_instance


def create_category(db: Session, category: schemas.CategoryCreate):
    return create_instance(db, models.Category, category)


def get_categories(db: Session):
    return get_all_instances(db, models.Category)


def get_category_by_id(db: Session, category_id: str):
    return get_instance_by_id(db, models.Category, category_id)


def update_category(db: Session, category_id: str, category_update: schemas.CategoryUpdate):
    return update_instance(db, models.Category, category_id, category_update)


def delete_category(db: Session, category_id: str):
    return delete_instance(db, models.Category, category_id)
