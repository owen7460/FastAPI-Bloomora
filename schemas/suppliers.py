

from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator


class SupplierCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=1, max_length=150, strict=True)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=1, max_length=30)
    contact_name: str | None = Field(default=None, min_length=1, max_length=150)
    is_active: bool = True
    note: str | None = Field(default=None, min_length=1, max_length=255)


class SupplierUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str | None = Field(default=None, min_length=1, max_length=150)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, min_length=1, max_length=30)
    contact_name: str | None = Field(default=None, min_length=1, max_length=150)
    is_active: bool | None = None
    note: str | None = Field(default=None, min_length=1, max_length=255)

    @field_validator(
        "name",
        "is_active"
)

    @classmethod
    def prevent_null(cls, value):
        if value is None:
            raise ValueError("This field cannot be null")
        return value