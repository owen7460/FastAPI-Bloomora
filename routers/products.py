from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from crud import products
from schemas.products import ProductCreate, ProductUpdate
from services import products as product_service
from services.products import DuplicateSKUError

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


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    try:
        product_data = await product_service.create_product(db, product)
    except DuplicateSKUError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))

    return {
        "code": 201,
        "message": "create product successfully",
        "data": product_data,
    }


@router.patch("/{product_id}")
async def update_product(
    product_id: int, product: ProductUpdate, db: AsyncSession = Depends(get_db)
):
    updated_product = await products.update_product(db, product_id, product)

    if updated_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    return {
        "code": 200,
        "message": "update product successfully",
        "data": updated_product,
    }


@router.delete("/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    deleted_product = await products.delete_product(db, product_id)

    if deleted_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    return {
        "code": 200,
        "message": "delete product successfully",
        "data": deleted_product,
    }
