from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from config.db_conf import get_db
from dependencies.auth import get_current_user
from models.suppliers import Supplier
from models.users import User
from crud import suppliers
from schemas.suppliers import SupplierCreate, SupplierUpdate

router = APIRouter(prefix="/api/suppliers", tags=["Suppliers"])

@router.get("/{supplier_id}", status_code=200)
async def get_supplier(
        supplier_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    supplier_data = await suppliers.get_supplier_by_id(db, supplier_id)
    if supplier_data is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    return {
        "code": 200,
        "message": "success",
        "data": supplier_data
    }

@router.get("/", )
async def get_suppliers(
        page: int = 1,
        page_size: int = Query(25, alias="pageSize"),
        db: AsyncSession = Depends(get_db),
        current_user : User = Depends(get_current_user)
):
    skip = (page - 1) * page_size
    limit = page_size

    suppliers_data = await suppliers.get_suppliers(db, skip, limit)

    return {
        "code": 200,
        "message": "success",
        "data": suppliers_data
    }


@router.post("/", status_code=201)
async def create_supplier(
        supplier: SupplierCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    created_supplier = await suppliers.create_supplier(db, supplier)

    return {
        "code": 201,
        "message": "create supplier successfully",
        "data": created_supplier
    }


@router.patch("/{supplier_id}", status_code=200)
async def update_supplier(
        supplier: SupplierUpdate,
        supplier_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    updated_supplier = await suppliers.update_supplier(db, supplier_id, supplier)

    return {
        "code": 200,
        "message": "update supplier successfully",
        "data": updated_supplier
    }


@router.delete("/{supplier_id}")
async def delete_supplier(
        supplier_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    deleted_supplier = await suppliers.delete_supplier(db, supplier_id)

    if deleted_supplier is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Supplier not found")

    return {
        "code": 200,
        "message": "delete supplier successfully",
        "data": deleted_supplier
    }