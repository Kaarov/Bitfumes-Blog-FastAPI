from fastapi import FastAPI
from . import schemas

app = FastAPI()


@app.post("/")
def create(request: schemas.Blog):
    return request
