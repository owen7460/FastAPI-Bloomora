import asyncio

from config.db_conf import async_engine
from models.base import Base

from models.users import User
from models.products import Product
from models.announcements import Announcement

async def create_tables():
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        print("Database tables created successfully!")

    finally:
        await async_engine.dispose()


if __name__ == "__main__":
    asyncio.run(create_tables())