from typing import List
from models import Product
import schemas

def get_product_info(product: Product):
    return schemas.ProductLiteResponse(
        id = getattr(product, 'id', None),
        category_id=getattr(product, 'category_id', None),
        category_name=getattr(product.category, 'name', None),
        generic_name=getattr(product, 'generic_name', ""),
        image_url=getattr(product, 'image_url', None),
        description=getattr(product, 'description', None),
        availability=getattr(product, 'availability', False),
        is_best_seller=getattr(product, 'is_best_seller', False),
        brand_name=getattr(product, 'brand_name', None),
        manufacturer=getattr(product, 'manufacturer', None),
        composition=getattr(product, 'composition', None),
        supply_type=getattr(product, 'supply_type', None),
        details=schemas.ProductDetailResponse(
            product_id=product.product_details[0].product_id,
            strength=product.product_details[0].strength,
            other_brand_names=product.product_details[0].other_brand_names,
            other_presentations=product.product_details[0].other_presentations,
        ) if product.product_details else None
    )
    
def get_list_product_info(products: List[Product]):
    return [get_product_info(product) for product in products]