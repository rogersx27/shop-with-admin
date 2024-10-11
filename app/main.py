from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.models import categoryRouter, customerRouter, orderRouter, orderItemRouter, productRouter, productDetailRouter

from routes.pages import homeRouter
from routes.admin import adminRouter
from routes.admin import adminRouter2

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(categoryRouter.router, prefix="/api")
app.include_router(customerRouter.router, prefix="/api")
app.include_router(orderRouter.router, prefix="/api")
app.include_router(orderItemRouter.router, prefix="/api")
app.include_router(productRouter.router, prefix="/api")
app.include_router(productDetailRouter.router, prefix="/api")
app.include_router(homeRouter.router)
app.include_router(adminRouter.router)
app.include_router(adminRouter2.router)


