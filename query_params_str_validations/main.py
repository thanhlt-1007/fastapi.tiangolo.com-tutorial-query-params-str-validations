from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def get_hello():
    return {
        "message": "Hello, World!"
    }

@app.get("/items")
async def get_items(q: str | None = None):
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
