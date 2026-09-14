from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import products, auth

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello from Bloomora"}


app.include_router(products.router)
app.include_router(auth.router)
