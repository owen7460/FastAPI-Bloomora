from sqlalchemy.ext.asyncio import AsyncSession

from crud.users import get_user_by_email, create_user
from schemas.users import UserCreate

class DuplicateEmailError(Exception):
    def __init__(self, email: str):
        super().__init__(f"Email '{email}' already registered")

async def register_user(db: AsyncSession, user: UserCreate):
    existing_user = await get_user_by_email(db, user.email)

    if existing_user is not None:
        raise DuplicateEmailError(user.email)

    return await create_user(db, user)