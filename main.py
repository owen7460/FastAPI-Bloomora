from fastapi import FastAPI

from routers import products

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from Bloomora"}


app.include_router(products.router)
