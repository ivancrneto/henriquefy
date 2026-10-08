from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/orders")
def create():
    return JSONResponse(content={"id": 1}, status_code=201)
