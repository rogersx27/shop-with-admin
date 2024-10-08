import random
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
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
        raise HTTPException(status_code=404, detail="Not enough products to show")

    five_products = random.sample(all_products, num_products)

    return five_products


def get_all_products_by_first_letter(db: Session, letter: str):
    # Validación simplificada de la letra
    if not letter.isalpha() or len(letter) != 1:
        raise HTTPException(status_code=400, detail="Invalid letter. Please provide a single letter from a-z")

    products = db.query(models.Product).options(
        joinedload(models.Product.product_details)
        ).filter(models.Product.generic_name.ilike(f"{letter}%")).all()

    if not products:
        raise HTTPException(status_code=404, detail="No products found")

    # Generar la respuesta con comprensión de listas
    products_info = [
        schemas.ProductLiteResponse(
            category_id=getattr(product, 'category_id', None),
            generic_name=getattr(product, 'generic_name', ""),
            image_url=getattr(product, 'image_url', None),
            description=getattr(product, 'description', None),
            availability=getattr(product, 'availability', False),
            details=schemas.ProductDetailResponse(
                product_id=product.product_details[0].product_id,
                brand_name=product.product_details[0].brand_name,
                strength=product.product_details[0].strength,
                composition=product.product_details[0].composition,
                supply_type=product.product_details[0].supply_type,
                manufacturer=product.product_details[0].manufacturer,
                other_brand_names=product.product_details[0].other_brand_names,
                price=product.product_details[0].price,
                stock=product.product_details[0].stock
            ) if product.product_details else None
        )
        for product in products
    ]
    return products_info
