from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    sku: str
    description: str | None = None
    category_id: int | None = None
    price: Decimal
    cost_price: Decimal | None = None
    stock_quantity: int = 0
    low_stock_threshold: int = 10
    unit: str = "item"
    image_url: str | None = None
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: str | None = None
    sku: str | None = None
    description: str | None = None
    category_id: int | None = None
    price: Decimal | None = None
    cost_price: Decimal | None = None
    stock_quantity: int | None = None
    low_stock_threshold: int | None = None
    unit: str | None = None
    image_url: str | None = None
    is_active: bool | None = None

    model_config = ConfigDict(from_attributes=True)