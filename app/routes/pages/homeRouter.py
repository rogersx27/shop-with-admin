from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from database import get_db
import services.category
import services.product

templates = Jinja2Templates(directory="templates")
router = APIRouter(tags=["Pages"])


@router.get("/home/", response_class=HTMLResponse)
def get_categories(request: Request, db: Session = Depends(get_db)):
    category_responses = services.category.get_categories_with_products(db=db)
    letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    best_sellers = services.product.get_best_sellers_by_field(db=db)
    
    context = {
        "request": request,
        "categories": category_responses,
        "letters": letters,
        "best_sellers": best_sellers
    }

    return templates.TemplateResponse("index.html", context)


@router.get("/products/start/{letter}/", response_class=HTMLResponse)
def get_products_by_letter(request: Request, letter: str, db: Session = Depends(get_db)):
    product_with_letter = services.product.get_all_products_by_first_letter(
        db=db, letter=letter)

    return templates.TemplateResponse("productsLetter.html", {"request": request, "products": product_with_letter, "letter": letter})
