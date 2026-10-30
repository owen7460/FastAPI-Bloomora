from sqlalchemy import Text, String, text, ForeignKey, Boolean
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Announcement(Base):
    __tablename__ = "announcements"

    id: Mapped[int] = mapped_column(
        BIGINT(unsigned=True),
        primary_key=True,
        autoincrement=True,
        comment="announcement_id",
    )

    title: Mapped[str] = mapped_column(
        String(200),
        comment="announcement_title",
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        comment="announcement_content",
        nullable=False,
    )

    is_published: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("0")
    )

    is_pinned: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default=text("0")
    )

    created_by: Mapped[int] = mapped_column(
        BIGINT(unsigned=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    def __repr__(self):
        return f"<Announcement id={self.id} title={self.title}>"
