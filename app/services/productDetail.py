import uuid
from sqlalchemy.orm import Session
import schemas
import models

from .general import (
    create_instance,
    delete_instance,
    get_all_instances,
    get_instance_by_id,
    update_instance,
    create_instance_only,
)


def create_productDetail(db: Session, productDetail: schemas.ProductDetailCreate):
    return create_instance(db, models.ProductDetail, productDetail)


def create_productDetail_only(db: Session, productDetail: schemas.ProductDetailCreate):
    return create_instance_only(db, models.ProductDetail, productDetail)


def get_productDetails(db: Session):
    return get_all_instances(db, models.ProductDetail)


def get_productDetail_by_id(db: Session, productDetail_id: str | uuid.UUID):
    return get_instance_by_id(db, models.ProductDetail, productDetail_id)


def update_productDetail(
    db: Session,
    productDetail_id: str | uuid.UUID,
    productDetail_update: schemas.ProductDetailUpdate,
):
    return update_instance(
        db, models.ProductDetail, productDetail_id, productDetail_update
    )


def delete_productDetail(db: Session, productDetail_id: str | uuid.UUID):
    return delete_instance(db, models.ProductDetail, productDetail_id)


def get_productDetails_by_product_id(db: Session, product_id: str | uuid.UUID):
    return (
        db.query(models.ProductDetail)
        .filter(models.ProductDetail.product_id == product_id)
        .all()
    )
