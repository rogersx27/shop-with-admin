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
def add_category_form(request: Request, db: Session = Depends(get_db)):
    categories = services.category.get_categories(db)  # Obtener categorías para mostrar
    return templates.TemplateResponse(
        "add_category.html", {"request": request, "categories": categories}
    )

@router.post("/admin/add-category/")
async def add_category(
    request: Request, db: Session = Depends(get_db), name: str = Form(...),
):
    try:
        services.category.create_category(db, schemas.CategoryCreate(name=name))
        message = "Categoría agregada con éxito"
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creando categoría: {str(e)}")

    categories = services.category.get_categories(db)
    products = services.product.get_products(db)

    return templates.TemplateResponse(
        "add_product.html",
        {
            "request": request,
            "categories": categories,
            "products": products,
            "message": message,
        },
    )


@router.get("/admin/add-product/", response_class=HTMLResponse)
def add_product_form(request: Request, db: Session = Depends(get_db)):
    categories = services.category.get_categories(db)
    products = services.product.get_products(db)

    return templates.TemplateResponse(
        "add_product.html",
        {"request": request, "categories": categories, "products": products},
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
):
    try:
        # Crear un nuevo producto
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
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creando producto: {str(e)}")

    # Obtener las categorías y productos actualizados
    categories = services.category.get_categories(db)
    products = services.product.get_products(db)

    # Retornar la plantilla actualizada con los productos nuevos
    return templates.TemplateResponse(
        "add_product.html",
        {
            "request": request,
            "message": "Producto agregado con éxito",
            "categories": categories,
            "products": products,
        },
    )


@router.post("/admin/add-product-detail/")
async def add_product_detail(
    request: Request,
    db: Session = Depends(get_db),
    product_id: UUID = Form(...),
    strength: str = Form(...),
    other_brand_names: str = Form(None),
    packaging: str = Form(None),
    other_presentations: str = Form(None),
):
    parsed_other_presentations = None
    if other_presentations:
        try:
            parsed_other_presentations = json.loads(other_presentations)
        except json.JSONDecodeError:
            categories = services.category.get_categories(db)
            products = services.product.get_products(db)
            return templates.TemplateResponse(
                "add_product.html",
                {
                    "request": request,
                    "message": "Error: El formato de 'Otras Presentaciones' no es válido.",
                    "categories": categories,
                    "products": products,
                },
            )

    try:
        new_product_detail = services.productDetail.create_productDetail_only(
            db,
            schemas.ProductDetailCreate(
                product_id=product_id,
                strength=strength,
                packaging=packaging,
                other_presentations=parsed_other_presentations,
            ),
        )
        db.add(new_product_detail)
        db.commit()
        db.refresh(new_product_detail)
        message = "Detalles del producto agregados con éxito"
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Error creando detalles del producto: {str(e)}"
        )

    categories = services.category.get_categories(db)
    products = services.product.get_products(db)

    return templates.TemplateResponse(
        "add_product.html",
        {
            "request": request,
            "message": message,
            "categories": categories,
            "products": products,
        },
    )
