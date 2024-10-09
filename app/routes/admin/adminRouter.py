import json
from uuid import UUID
from fastapi import APIRouter, HTTPException, Request, Form, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import get_db
from fastapi.templating import Jinja2Templates

import services
import schemas

templates = Jinja2Templates(directory="templates")
router = APIRouter(tags=["Admin"])


@router.get("/admin/categories/", response_class=HTMLResponse)
def list_categories(request: Request, db: Session = Depends(get_db)):
    categories = services.category.get_categories(db)
    return templates.TemplateResponse(
        "list_categories.html", {"request": request, "categories": categories}
    )


@router.get("/admin/add-category/", response_class=HTMLResponse)
def add_category_form(request: Request):
    return templates.TemplateResponse("add_category.html", {"request": request})


@router.post("/admin/add-category/")
async def add_category(
    request: Request, db: Session = Depends(get_db), name: str = Form(...)
):
    services.category.create_category(db, schemas.CategoryCreate(name=name))
    return templates.TemplateResponse(
        "add_category.html",
        {"request": request, "message": "Categoría agregada con éxito"},
    )


@router.get("/admin/products/", response_class=HTMLResponse)
def list_products(request: Request, db: Session = Depends(get_db)):
    categories = services.category.get_categories(db)
    return templates.TemplateResponse(
        "add_product.html", {"request": request, "categories": categories}
    )


@router.get("/admin/add-product/", response_class=HTMLResponse)
def add_product_form(request: Request, db: Session = Depends(get_db)):
    categories = services.category.get_categories(db)
    return templates.TemplateResponse(
        "add_product.html", {"request": request, "categories": categories}
    )


@router.post("/admin/add-product/")
async def add_product(
    request: Request,
    db: Session = Depends(get_db),
    generic_name: str = Form(...),
    category_id: UUID = Form(...),
    description: str = Form(None),
    image_url: str = Form(None),
    availability: bool = Form(True),
    is_best_seller: bool = Form(False),
    large_description: str = Form(None),
    brand_name: str = Form(...),
    strength: str = Form(...),
    composition: str = Form(None),
    supply_type: str = Form(...),
    manufacturer: str = Form(...),
    other_brand_names: str = Form(None),
    price: float = Form(...),
    stock: int = Form(...),
    packaging: str = Form(None),
    quantity_per_pack: str = Form(None),
    other_presentations: str = Form(None),
):
    categories = services.category.get_categories(db)
    try:
        new_product = services.product.create_product_only(
            db,
            schemas.ProductCreate(
                generic_name=generic_name,
                category_id=category_id,
                description=description,
                image_url=image_url,
                availability=availability,
                is_best_seller=is_best_seller,
                large_description=large_description,
            ),
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creando producto: {str(e)}")

    parsed_other_presentations = None
    if other_presentations:
        try:
            parsed_other_presentations = json.loads(other_presentations)  # Convertir la cadena en JSON
        except json.JSONDecodeError:
            return templates.TemplateResponse(
                "add_product.html",
                {
                    "request": request,
                    "message": "Error: El formato de 'Otras Presentaciones' no es válido.",
                    "categories": categories,
                },
            )

    try:
        new_product_detail = services.productDetail.create_productDetail_only(
            db,
            schemas.ProductDetailCreate(
                product_id=getattr(new_product, "id"),
                brand_name=brand_name,
                strength=strength,
                composition=composition,
                supply_type=supply_type,
                manufacturer=manufacturer,
                other_brand_names=other_brand_names,
                price=price,
                stock=stock,
                packaging=packaging,
                quantity_per_pack=quantity_per_pack,
                other_presentations=parsed_other_presentations,
            ),
        )

    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error creando detalles del producto: {str(e)}"
        )

    db.add(new_product)
    db.add(new_product_detail)
    db.commit()
    db.refresh(new_product)
    db.refresh(new_product_detail)
    
    print(other_presentations)

    return templates.TemplateResponse(
        "add_product.html",
        {
            "request": request,
            "message": "Producto agregado con éxito",
            "categories": categories,
        },
    )
