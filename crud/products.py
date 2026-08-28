from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.products import Products
from schemas.products import ProductCreate

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 10):
    stmt = select(Products).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()

async def create_product(db:AsyncSession, product: ProductCreate):
    product_obj = Products(**product.model_dump())
    db.add(product_obj)
    await db.flush()
    await db.refresh(product_obj)
    return product_obj