from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import uuid

import models
from schemas import *

from schemas import CategoryCreate, CategoryResponse, ProductCreate, ProductResponse, CustomerCreate, CustomerResponse, OrderCreate, OrderResponse, OrderItemCreate, OrderItemResponse
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


### CRUD de Categorías ###


@app.post("/categories/", response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(id=str(uuid.uuid4()), name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.get("/categories/", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


### CRUD de Productos ###


@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(
        models.Category.id == product.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db_product = models.Product(
        id=str(uuid.uuid4()),
        name=product.name,
        category_id=product.category_id,
        price=product.price,
        description=product.description,
        image_url=product.image_url,
        quantity=product.quantity,
        availability=product.availability
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.get("/products/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()


@app.get("/products/{product_id}/", response_model=ProductResponse)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


### CRUD de Clientes ###


@app.post("/customers/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(
        id=str(uuid.uuid4()),
        name=customer.name,
        email=customer.email,
        address=customer.address,
        phone=customer.phone
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@app.get("/customers/", response_model=List[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

### CRUD de Pedidos ###


@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(
        models.Customer.id == order.customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    db_order = models.Order(
        id=str(uuid.uuid4()),
        customer_id=order.customer_id,
        status=order.status
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@app.get("/orders/", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()


@app.get("/orders/{order_id}/", response_model=OrderResponse)
def get_order(order_id: str, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


### CRUD de Elementos de Pedidos ###


@app.post("/order_items/", response_model=OrderItemResponse)
def create_order_item(order_item: OrderItemCreate, db: Session = Depends(get_db)):
    # Verificar si el pedido y el producto existen
    order = db.query(models.Order).filter(
        models.Order.id == order_item.order_id).first()
    product = db.query(models.Product).filter(
        models.Product.id == order_item.product_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db_order_item = models.OrderItem(
        id=str(uuid.uuid4()),
        order_id=order_item.order_id,
        product_id=order_item.product_id,
        quantity=order_item.quantity,
        price=order_item.price
    )
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item


@app.get("/order_items/", response_model=List[OrderItemResponse])
def get_order_items(db: Session = Depends(get_db)):
    return db.query(models.OrderItem).all()
