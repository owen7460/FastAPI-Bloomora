from fastapi import APIRouter

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def get_products(skip: int = 0, limit: int = 10):
    return {
        "code": 200,
        "message": "get products successfully",
        "data": "get products info",
    }
