from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from models.announcements import Announcement
from schemas.announcements import AnnouncementCreate, AnnouncementUpdate

async def get_announcement_by_id(db: AsyncSession, announcement_id: int) -> Announcement| None:
    stmt = select(Announcement).where(Announcement.id == announcement_id)
    result = await db.execute(stmt)
    announcement = result.scalar_one_or_none()
    return announcement

async def get_announcements(db: AsyncSession) -> list[Announcement]:
    stmt = select(Announcement).order_by(Announcement.is_pinned.desc(),
                                         Announcement.created_at.desc(),
                                         Announcement.id.desc())
    result = await db.execute(stmt)
    return list(result.scalars().all())

async def create_announcement(db: AsyncSession, announcement: AnnouncementCreate, created_by: int) -> Announcement:
    announcement_obj = Announcement(
        **announcement.model_dump(),
        created_by = created_by
    )
    db.add(announcement_obj)
    await db.flush()
    await db.refresh(announcement_obj)
    return announcement_obj

async def update_announcement(db: AsyncSession, announcement_id: int, announcement: AnnouncementUpdate) -> Announcement | None:
    announcement_obj = await get_announcement_by_id(db, announcement_id)
    if announcement_obj is None:
        return None

    update_data = announcement.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(announcement_obj, field, value)

    await db.flush()
    await db.refresh(announcement_obj)
    return announcement_obj

async def delete_announcement(db: AsyncSession, announcement_id: int) -> Announcement | None:
    announcement_obj = await get_announcement_by_id(db, announcement_id)

    if announcement_obj is None:
        return None

    await db.delete(announcement_obj)
    await db.flush()

    return announcement_obj
