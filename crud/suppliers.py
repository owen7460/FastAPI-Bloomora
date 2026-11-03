from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.suppliers import SupplierCreate, SupplierUpdate
from models.suppliers import Supplier


async def get_supplier_by_id(db: AsyncSession, supplier_id: int) -> Supplier | None:
    return await db.get(Supplier, supplier_id)


async def get_suppliers(db: AsyncSession, skip: int = 0, limit: int = 25) -> list[Supplier]:
    stmt = select(Supplier).offset(skip).limit(limit).order_by(Supplier.created_at.desc(), Supplier.id.desc())
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def create_supplier(db: AsyncSession, supplier: SupplierCreate) -> Supplier:
    supplier_obj = Supplier(**supplier.dict())
    db.add(supplier_obj)
    await db.commit()
    await db.refresh(supplier_obj)
    return supplier_obj


async def update_supplier(db: AsyncSession, supplier_id: int, supplier: SupplierUpdate) -> Supplier | None:
    stmt = select(Supplier).where(Supplier.id == supplier_id)
    result = await db.execute(stmt)
    supplier_obj = result.scalar_one_or_none()

    if supplier_obj is None:
        return None

    update_data = supplier.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(supplier_obj, field, value)

    await db.flush()
    await db.refresh(supplier_obj)

    return supplier_obj


async def delete_supplier(db: AsyncSession, supplier_id: int) -> Supplier | None:
    stmt = select(Supplier).where(Supplier.id == supplier_id)
    result = await db.execute(stmt)
    supplier_obj = result.scalar_one_or_none()

    if supplier_obj is None:
        return None

    await db.delete(supplier_obj)
    await db.flush()

    return supplier_obj