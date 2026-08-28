from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.products import Products


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 10):
    stmt = select(Products).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()
