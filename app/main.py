from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routes.models import categoryRouter

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(categoryRouter.router, prefix="/api")


@app.get("/")
def read_root():
    return {"Hello": "World"}
