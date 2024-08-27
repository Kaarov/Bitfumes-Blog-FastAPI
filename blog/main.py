from fastapi import FastAPI
from . import schemas, models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post("/")
def create(request: schemas.Blog):
    return request
