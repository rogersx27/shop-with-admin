from models import Product
import schemas

def get_product_info(product: Product):
    return schemas.ProductLiteResponse(
        id = getattr(product, 'id', None),
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
    
def get_list_product_info(products):
    return [get_product_info(product) for product in products]