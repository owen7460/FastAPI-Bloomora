from sqlalchemy.ext.asyncio import AsyncSession

from crud import products as product_crud
from schemas.products import ProductCreate


class DuplicateSKUError(Exception):
    def __init__(self, sku: str):
        super().__init__(f"SKU'{sku}' already exists")


async def create_product(db: AsyncSession, product: ProductCreate):
    existing_product = await product_crud.get_product_by_sku(db, product.sku)

    if existing_product is not None:
        raise DuplicateSKUError(product.sku)

    return await product_crud.create_product(db, product)
