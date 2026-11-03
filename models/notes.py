from sqlalchemy import String, Text, ForeignKey, Boolean, text
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.users import User

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        comment="noteId",
    )

    title: Mapped[str] = mapped_column(String(150), nullable=False)

    author_id: Mapped[int] = mapped_column(BIGINT(unsigned=True), ForeignKey("users.id") ,nullable=False)

    content: Mapped[str] = mapped_column(Text, nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=text("1"))

    author: Mapped["User"] = relationship(back_populates="notes")

    def __repr__(self):
        return f"<Note {self.id} - {self.title}>"




