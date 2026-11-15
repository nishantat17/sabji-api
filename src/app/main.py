from fastapi import FastAPI
from scalar_fastapi import add_scalar_reference, Theme

app = FastAPI(
    title="Sabji API"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


add_scalar_reference(app, route="/docs/scalar", theme=Theme.MOON)