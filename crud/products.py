from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.products import Products
from schemas.products import ProductCreate, ProductUpdate

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

async def update_product(db:AsyncSession, product_id: int, product: ProductUpdate):
    stmt = select(Products).where( Products.id == product_id)
    result = await db.execute(stmt)
    product_obj = result.scalar_one_or_none()

    if product_obj is None:
        return None

    update_data = product.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(product_obj, field, value)

    await db.flush()
    await db.refresh(product_obj)

    return product_obj