

from pydantic import BaseModel, ConfigDict, Field, field_validator


class NoteCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=150,)

    content: str = Field(min_length=1, max_length=10000)

    is_active: bool = True


class NoteUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str | None = Field(default=None, min_length=1, max_length=150)

    content: str | None = Field(default=None, min_length=1, max_length=10000)

    is_active: bool | None = None

    @field_validator("title", "content", "is_active")
    @classmethod
    def prevent_null(cls, value):
        if value is None:
            raise ValueError("This field cannot be null")
        return value