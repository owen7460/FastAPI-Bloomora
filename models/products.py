from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, Numeric, String, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=text("CURRENT_TIMESTAMP"), comment="create_time"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        server_onupdate=text("CURRENT_TIMESTAMP"),
        comment="update_time",
    )


class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True, comment="productID"
    )

    name: Mapped[str] = mapped_column(String(150), nullable=False)

    sku: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    category_id: Mapped[int | None] = mapped_column(
        BIGINT(unsigned=True), nullable=True
    )

    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    cost_price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    stock_quantity: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), nullable=False, server_default=text("0")
    )

    low_stock_threshold: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), nullable=False, server_default=text("10")
    )

    unit: Mapped[str] = mapped_column(
        String(30), nullable=False, server_default=text("'item'")
    )

    image_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    is_active: Mapped[bool] = mapped_column(
        TINYINT(1), nullable=False, server_default=text("1")
    )

    def __repr__(self):
        return f"<Products(id={self.id}, name={self.name}"
