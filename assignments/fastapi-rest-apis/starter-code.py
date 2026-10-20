from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Inventory API")

items = [
    {"id": 1, "name": "Notebook", "price": 4.99},
    {"id": 2, "name": "Pencil", "price": 1.25},
]


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def home():
    return {"message": "Welcome to the Inventory API!"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    new_item = {"id": len(items) + 1, "name": item.name, "price": item.price}
    items.append(new_item)
    return new_item
