from decimal import Decimal

from pydantic import BaseModel


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