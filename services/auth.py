from sqlalchemy.ext.asyncio import AsyncSession

from crud.users import get_user_by_email, create_user
from schemas.users import UserCreate
from utils.security import verify_password, create_access_token


class DuplicateEmailError(Exception):
    def __init__(self, email: str):
        super().__init__(f"Email '{email}' already registered")


async def register_user(db: AsyncSession, user: UserCreate):
    existing_user = await get_user_by_email(db, user.email)

    if existing_user is not None:
        raise DuplicateEmailError(user.email)

    return await create_user(db, user)


async def _authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)

    if user is None:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user


async def login_user(db: AsyncSession, email: str, password: str):
    user = await _authenticate_user(db, email, password)

    if user is None:
        return None

    access_token = create_access_token({"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
