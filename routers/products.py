from fastapi import APIRouter

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/")
async def get_products():
    return {"msg": "get products info"}