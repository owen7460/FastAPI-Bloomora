from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.suppliers import SupplierCreate
from models.suppliers import Supplier


async def get_supplier_by_id(db: AsyncSession, supplier_id: int) -> Supplier | None:
    return await db.get(Supplier, supplier_id)

async def get_suppliers(db: AsyncSession) -> list[Supplier]:
    stmt = select(Supplier).order_by(Supplier.created_at.desc(),
        Supplier.id.desc())
    result = await db.execute(stmt)
    return list(result.scalars().all())

