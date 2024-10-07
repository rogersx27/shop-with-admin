from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from database import get_db
import services.category as service

templates = Jinja2Templates(directory="templates")
router = APIRouter(tags=["Pages"])


@router.get("/home/")
def get_categories(request: Request, db: Session = Depends(get_db)):
    category_responses = service.get_categories_with_products(db=db)

    return templates.TemplateResponse("index.html", {"request": request, "categories": category_responses})
