from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

class AnnouncementBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1)

class AnnouncementCreate(AnnouncementBase):
    is_published: bool = False
    is_pinned: bool = False

class AnnouncementUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = Field(default=None, min_length=1)
    is_published: bool | None = None
    is_pinned: bool | None = None

    @field_validator(
        "title",
        "content",
        "is_published",
        "is_pinned"
    )

    @classmethod
    def prevent_null(cls, value):
        if value is None:
            raise ValueError("This field cannot be null")
        return value

class AnnouncementResponse(AnnouncementBase):
    id:int
    is_published: bool
    is_pinned: bool
    created_by: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)