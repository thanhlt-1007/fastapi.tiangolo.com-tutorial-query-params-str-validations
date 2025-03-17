from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/hello")
async def get_hello():
    return {
        "message": "Hello, World!"
    }

@app.get("/items")
async def get_items(
    q: Annotated[str | None, Query(max_length=50)] = None,
):
    items = {
        "items": [
            {
                "item_id": "Foo",
            },
            {
                "item_id": "Bar",
            }
        ]
    }

    if q:
        items.update({"q": q})

    return items
