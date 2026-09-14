from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.products import Product
from schemas.products import ProductCreate, ProductUpdate


async def get_product_by_sku(db: AsyncSession, sku: str):
    stmt = select(Product).where(Product.sku == sku)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 20):
    stmt = select(Product).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def create_product(db: AsyncSession, product: ProductCreate):
    product_obj = Product(**product.model_dump())
    db.add(product_obj)
    await db.flush()
    await db.refresh(product_obj)
    return product_obj


async def update_product(db: AsyncSession, product_id: int, product: ProductUpdate):
    stmt = select(Product).where(Product.id == product_id)
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


async def delete_product(db: AsyncSession, product_id: int):
    stmt = select(Product).where(Product.id == product_id)
    result = await db.execute(stmt)
    product_obj = result.scalar_one_or_none()

    if product_obj is None:
        return None

    await db.delete(product_obj)
    await db.flush()

    return product_obj
