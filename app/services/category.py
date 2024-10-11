from typing import List
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
)


def create_category(db: Session, category: schemas.CategoryCreate):
    return create_instance(db, models.Category, category)


def get_categories(db: Session):
    return get_all_instances(db, models.Category)


def get_category_by_id(db: Session, category_id: str):
    return get_instance_by_id(db, models.Category, category_id)


def update_category(
    db: Session, category_id: str, category_update: schemas.CategoryUpdate
):
    return update_instance(db, models.Category, category_id, category_update)


def delete_category(db: Session, category_id: str | uuid.UUID):
    return delete_instance(db, models.Category, category_id)


def get_categories_with_products(
    db: Session,
) -> List[schemas.CategoryWithProductsResponse]:
    categories = get_categories(db)

    category_responses: List[schemas.CategoryWithProductsResponse] = []
    for category in categories:
        products = []
        for product in category.products:
            product_details = (
                schemas.ProductDetailBase(
                    product_id=product.product_details[0].product_id,
                    strength=product.product_details[0].strength,
                    composition=product.product_details[0].composition,
                    other_brand_names=product.product_details[0].other_brand_names,
                    price=product.product_details[0].price,
                )
                if product.product_details
                else None
            )

            products.append(
                schemas.ProductLiteResponse(
                    generic_name=product.generic_name,
                    image_url=product.image_url,
                    description=product.description,
                    availability=product.availability,
                    is_best_seller=product.is_best_seller,
                    brand_name=product.brand_name,
                    manufacturer=product.manufacturer,
                    composition=product.composition,
                    supply_type=product.supply_type,
                    details=product_details,
                )
            )

        category_responses.append(
            schemas.CategoryWithProductsResponse(
                id=category.id,
                name=category.name,
                products=products,
            )
        )

    #  category_responses_2: List[schemas.CategoryWithProductsResponse] = [schemas.CategoryWithProductsResponse.model_validate(category) for category in categories]

    return category_responses
