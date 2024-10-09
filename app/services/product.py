import random
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
import utils.utils as utils
import schemas
import models

from .general import (
    create_instance,
    delete_instance,
    get_all_instances,
    get_instance_by_id,
    update_instance,
)


def create_product(db: Session, product: schemas.ProductCreate):
    return create_instance(db, models.Product, product)


def get_products(db: Session):
    return get_all_instances(db, models.Product)


def get_product_by_id(db: Session, product_id: str) -> models.Product:
    return get_instance_by_id(db, models.Product, product_id)


def update_product(db: Session, product_id: str, product_update: schemas.ProductUpdate):
    return update_instance(db, models.Product, product_id, product_update)


def delete_product(db: Session, product_id: str):
    return delete_instance(db, models.Product, product_id)


def get_best_sellers_by_field(db: Session):
    products = (
        db.query(models.Product)
        .options(joinedload(models.Product.product_details))
        .filter(models.Product.is_best_seller == True)
        .all()
    )

    # if not products:
    #     raise HTTPException(status_code=404, detail="No best sellers found")

    products_info = utils.get_list_product_info(products)

    return products_info


def get_best_sellers_by_sales(db: Session):
    products = (
        db.query(models.Product)
        .options(joinedload(models.Product.product_details))
        .filter(models.Product.order_items != None)
        .all()
    )

    products.sort(key=lambda x: len(x.order_items), reverse=True)

    # if not products:
    #     raise HTTPException(status_code=404, detail="No best sellers found")

    products_info = utils.get_list_product_info(products)

    return products_info[:5]


def get_random_products(db: Session, num_products: int):
    all_products = get_products(db)

    if len(all_products) < num_products:
        raise HTTPException(status_code=404, detail="Not enough products to show")

    five_products = random.sample(all_products, num_products)

    products_info = utils.get_list_product_info(five_products)

    return products_info


def get_all_products_by_first_letter(db: Session, letter: str):
    if not letter.isalpha() or len(letter) != 1:
        raise HTTPException(
            status_code=400,
            detail="Invalid letter. Please provide a single letter from a-z",
        )

    products = (
        db.query(models.Product)
        .options(joinedload(models.Product.product_details))
        .filter(models.Product.generic_name.ilike(f"{letter}%"))
        .all()
    )

    # if not products:
    #     raise HTTPException(status_code=404, detail="No products found")

    products_info = products_info = utils.get_list_product_info(products)
    return products_info


def get_products_by_category(db: Session, category_id: str):
    products = (
        db.query(models.Product)
        .options(joinedload(models.Product.product_details))
        .filter(models.Product.category_id == category_id)
        .all()
    )

    # if not products:
    #     raise HTTPException(status_code=404, detail="No products found")

    products_info = utils.get_list_product_info(products)
    return products_info
