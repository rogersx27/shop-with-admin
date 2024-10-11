import json
from fastapi import APIRouter, HTTPException, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic_core import to_json
from sqlalchemy.orm import Session
from database import get_db
from fastapi.templating import Jinja2Templates
from uuid import UUID

import services
import schemas

templates = Jinja2Templates(directory="templates")
router = APIRouter(tags=["Admin2"])

# Category CRUD operations

@router.get("/admin2/categories/", response_class=HTMLResponse)
def list_categories(request: Request, db: Session = Depends(get_db)):
    categories = services.category.get_categories(db)
    return templates.TemplateResponse(
        "category_crud.html", {"request": request, "categories": categories}
    )

@router.post("/admin2/add-category/")
async def add_or_update_category(
    request: Request, 
    db: Session = Depends(get_db), 
    category_id: str = Form(None),
    name: str = Form(...)
):
    try:
        if category_id:
            category = services.category.update_category(db, category_id, schemas.CategoryUpdate(name=name))
            message = "Category updated successfully"
        else:
            category = services.category.create_category(db, schemas.CategoryCreate(name=name))
            message = "Category added successfully"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing category: {str(e)}")

    return RedirectResponse(url="/admin2/categories/", status_code=303)

@router.post("/admin2/delete-category/")
async def delete_category(
    request: Request,
    db: Session = Depends(get_db),
    category_id: UUID = Form(...)
):
    try:
        services.category.delete_category(db, category_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting category: {str(e)}")

    return RedirectResponse(url="/admin2/categories/", status_code=303)

# Product CRUD operations

@router.get("/admin2/products/", response_class=HTMLResponse)
def list_products(request: Request, db: Session = Depends(get_db)):
    products = services.product.get_products(db)
    categories = services.category.get_categories(db)
    return templates.TemplateResponse(
        "product_crud.html", {"request": request, "products": products, "categories": categories}
    )

@router.post("/admin2/add-product/")
async def add_or_update_product(
    request: Request,
    db: Session = Depends(get_db),
    product_id: str = Form(None),
    generic_name: str = Form(...),
    category_id: UUID = Form(...),
    description: str = Form(None),
    large_description: str = Form(None),
    image_url: str = Form(None),
    availability: bool = Form(False),
    is_best_seller: bool = Form(False),
    brand_name: str = Form(...),
    manufacturer: str = Form(...),
    composition: str = Form(None),
    supply_type: str = Form(...)
):
    try:
        product_data = schemas.ProductCreate(
            generic_name=generic_name,
            category_id=category_id,
            description=description,
            large_description=large_description,
            image_url=image_url,
            availability=availability,
            is_best_seller=is_best_seller,
            brand_name=brand_name,
            manufacturer=manufacturer,
            composition=composition,
            supply_type=supply_type
        )
        
        if product_id:
            product = services.product.update_product(db, product_id, product_data) # type: ignore
            message = "Product updated successfully"
        else:
            product = services.product.create_product(db, product_data)
            message = "Product added successfully"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing product: {str(e)}")

    return RedirectResponse(url="/admin2/products/", status_code=303)

@router.post("/admin2/delete-product/")
async def delete_product(
    request: Request,
    db: Session = Depends(get_db),
    product_id: UUID = Form(...)
):
    try:
        services.product.delete_product(db, product_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting product: {str(e)}")

    return RedirectResponse(url="/admin2/products/", status_code=303)

# Product Detail CRUD operations

@router.get("/admin2/product-details/", response_class=HTMLResponse)
def list_product_details(request: Request, db: Session = Depends(get_db)):
    product_details = services.productDetail.get_productDetails(db)
    products = services.product.get_products(db)
    return templates.TemplateResponse(
        "product_detail_crud.html", {"request": request, "product_details": product_details, "products": products}
    )

@router.post("/admin2/add-product-detail/")
async def add_or_update_product_detail(
    request: Request,
    db: Session = Depends(get_db),
    product_detail_id: str = Form(None),
    product_id: UUID = Form(...),
    strength: str = Form(...),
    packaging: str = Form(None),
    other_presentations: str = Form(None)
):
    try:
        
        json_other_presentations = None
        print(other_presentations)
        if other_presentations:
            json_other_presentations = json.loads(other_presentations)
            print(json_other_presentations)
            
        
        product_detail_data = schemas.ProductDetailCreate(
            product_id=product_id,
            strength=strength,
            packaging=packaging,
            other_presentations=json_other_presentations
        )
        
        if product_detail_id:
            product_detail = services.productDetail.update_productDetail(db, product_detail_id, product_detail_data) # type: ignore
            message = "Product Detail updated successfully"
        else:
            product_detail = services.productDetail.create_productDetail(db, product_detail_data)
            message = "Product Detail added successfully"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing product detail: {str(e)}")

    return RedirectResponse(url="/admin2/product-details/", status_code=303)

@router.post("/admin2/delete-product-detail/")
async def delete_product_detail(
    request: Request,
    db: Session = Depends(get_db),
    product_detail_id: UUID = Form(...)
):
    try:
        services.productDetail.delete_productDetail(db, product_detail_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting product detail: {str(e)}")

    return RedirectResponse(url="/admin2/product-details/", status_code=303)