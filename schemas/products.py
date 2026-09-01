from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    sku: str = Field(min_length=1, max_length=50)
    description: str | None = None
    category_id: int | None = Field(default=None, gt=0)
    price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    cost_price: Decimal | None = Field(
        default=None, ge=0, max_digits=10, decimal_places=2
    )
    stock_quantity: int = Field(default=0, ge=0)
    low_stock_threshold: int = Field(default=10, ge=0)
    unit: str = Field(default="item", min_length=1, max_length=30)
    image_url: str | None = Field(default=None, max_length=500)
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=150)
    sku: str | None = Field(default=None, min_length=1, max_length=50)
    description: str | None = None
    category_id: int | None = Field(default=None, gt=0)
    price: Decimal | None = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    cost_price: Decimal | None = Field(
        default=None, ge=0, max_digits=10, decimal_places=2
    )
    stock_quantity: int | None = Field(defalut=None, ge=0)
    low_stock_threshold: int | None = Field(default=None, ge=0)
    unit: str | None = Field(default=None, min_length=1, max_length=30)
    image_url: str | None = Field(default=None, max_length=500)
    is_active: bool | None = None

    # model_config = ConfigDict(from_attributes=True)
