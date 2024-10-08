from random import randint
import random
from fastapi import HTTPException
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


def get_best_sellers_by_field(db: Session):
    return db.query(models.Product).filter(models.Product.is_best_seller == True).all()


def get_best_sellers_by_sales(db: Session):
    products = db.query(models.Product).filter(
        models.Product.order_items != None).all()

    products.sort(key=lambda x: len(x.order_items), reverse=True)

    if len(products) == 0:
        raise HTTPException(status_code=404, detail="No best sellers found")

    return products[:5]


def get_random_products(db: Session, num_products: int):
    all_products = get_products(db)

    if len(all_products) < num_products:
        raise HTTPException(
            status_code=404, detail="Not enough products to show")

    five_products = random.sample(all_products, num_products)

    return five_products
