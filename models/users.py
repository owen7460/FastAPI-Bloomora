from sqlalchemy import String
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.notes import Note

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True), primary_key=True, autoincrement=True
    )

    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )

    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    notes: Mapped[list["Note"]] = relationship(
        back_populates="author")

    def __repr__(self):
        return f"<User {self.id} - {self.email}>"
