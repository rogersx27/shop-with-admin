from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from database import get_db
import services.category
import services.product
import services.productDetail

templates = Jinja2Templates(directory="templates")
router = APIRouter(tags=["Pages"])


@router.get("/home/", response_class=HTMLResponse)
def get_categories(request: Request, db: Session = Depends(get_db)):
    category_responses = services.category.get_categories_with_products(db=db)
    best_sellers = services.product.get_best_sellers_by_field(db=db)
    random_products = services.product.get_random_products(db=db, num_products=1)

    letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

    context = {
        "request": request,
        "categories": category_responses,
        "letters": letters,
        "best_sellers": best_sellers,
        "random_products": random_products,
    }

    return templates.TemplateResponse("index.html", context)


@router.get("/products/start/{letter}/", response_class=HTMLResponse)
def get_products_by_letter(
    request: Request, letter: str, db: Session = Depends(get_db)
):
    product_with_letter = services.product.get_all_products_by_first_letter(
        db=db, letter=letter
    )

    return templates.TemplateResponse(
        "productsLetter.html",
        {"request": request, "products": product_with_letter, "letter": letter},
    )


@router.get("/products/by/category/{category_id}/", response_class=HTMLResponse)
def get_products_by_category(
    request: Request, category_id: str, db: Session = Depends(get_db)
):
    product_by_category = services.product.get_products_by_category(
        db=db, category_id=category_id
    )

    category = services.category.get_category_by_id(db=db, category_id=category_id)

    return templates.TemplateResponse(
        "productsCategory.html",
        {"request": request, "products": product_by_category, "category": category},
    )


@router.get("/product/{product_id}/", response_class=HTMLResponse)
def get_product(request: Request, product_id: str, db: Session = Depends(get_db)):
    category_responses = services.category.get_categories_with_products(db=db)
    product = services.product.get_product_by_id(db=db, product_id=product_id)     
    letters = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    products_with_detail = services.productDetail.get_productDetails_by_product_id(
        db=db, product_id=product_id
    )

    brands = {product_detail.brand_name for product_detail in products_with_detail}
    manufacturers = {product_detail.manufacturer for product_detail in products_with_detail}

    context = {
        "request": request,
        "categories": category_responses,
        "letters": letters,
        "product": product,
        "products_with_detail": products_with_detail,
        "brands": brands,
        "manufacturers": manufacturers,
    }
    
    for product_detail in products_with_detail:
        print(product_detail.strength)
        print(product_detail.supply_type)

    return templates.TemplateResponse("product.html", context)
