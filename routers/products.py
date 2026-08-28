from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from crud import products
from schemas.products import ProductCreate
router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("/")
async def get_products(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    products_data = await products.get_products(db, skip, limit)
    return {
        "code": 200,
        "message": "get products successfully",
        "data": products_data,
    }

@router.post("/")
async def post_product(
        product: ProductCreate, db:AsyncSession = Depends(get_db)
):
    product_data = await products.create_product(db, product)
    return {
        "code": 201,
        "message": "create product successfully",
        "data": product_data,
    }