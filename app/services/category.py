from typing import List
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


def get_categories_with_products(db: Session) -> List[schemas.CategoryWithProductsResponse]:
    categories = get_categories(db)

    category_responses: List[schemas.CategoryWithProductsResponse] = []
    for category in categories:
        products = []
        for product in category.products:
            product_details = (
                schemas.ProductDetailBase(
                    product_id=product.product_details[0].product_id,
                    brand_name=product.product_details[0].brand_name,
                    strength=product.product_details[0].strength,
                    composition=product.product_details[0].composition,
                    supply_type=product.product_details[0].supply_type,
                    manufacturer=product.product_details[0].manufacturer,
                    other_brand_names=product.product_details[0].other_brand_names,
                    price=product.product_details[0].price,
                    stock=product.product_details[0].stock,
                )
                if product.product_details
                else None
            )

            products.append(
                schemas.ProductLiteResponse(
                    name=product.generic_name,
                    image_url=product.image_url,
                    description=product.description,
                    availability=product.availability,
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
        
    return category_responses
