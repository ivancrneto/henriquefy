from fastapi import FastAPI

app = FastAPI()


@app.post("/create_order")
def create_order():
    return {}


@app.get("/orders/{pk}")
def detail(pk: int):
    return {}
