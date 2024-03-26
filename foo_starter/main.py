from typing import Union
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def index():
    return {"hi": "api"}
@app.get("/item/{id}")
def item(id: int, q: Union[str, None] = None):
    return {"id": id, "query": q}
