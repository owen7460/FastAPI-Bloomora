from sqlalchemy import String, Boolean, text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base

class Supplier(Base):

    __tablename__ = "suppliers"

    id : Mapped[int] = mapped_column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True, comment="supplierID"
    )

    name: Mapped[str] = mapped_column(String(150), nullable=False)

    email: Mapped[str | None] = mapped_column(String(255), nullable=True)

    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)

    contact_name: Mapped[str | None] = mapped_column(String(150), nullable=True)

    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("1")
    )

    note: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def __repr__(self):
        return f"<Supplier(id={self.id}>, name={self.name!r})>"