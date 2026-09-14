from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.users import User
from schemas.users import UserCreate
from utils.security import hash_password

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(
        select(User).where(User.email == email)
    )

    return result.scalar_one_or_none()


async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user: UserCreate):
    user_data = user.model_dump(exclude={"password"})

    db_user = User(
        **user_data,
        hashed_password = hash_password(user.password)
    )

    db.add(db_user)
    await db.flush()
    await db.refresh(db_user)

    return db_user

