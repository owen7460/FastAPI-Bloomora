from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Note
from schemas.notes import NoteCreate, NoteUpdate


async def get_note_by_id(
        db: AsyncSession,
        note_id: int,
)-> Note | None:
    return await db.get(Note, note_id)


async def get_notes(db: AsyncSession, skip: int = 0, limit: int = 25) -> list[Note]:
    stmt = select(Note).offset(skip).limit(limit).order_by(Note.created_at.desc())
    result = await db.execute(stmt)

    return list(result.scalars().all())


async def create_note(db: AsyncSession, note: NoteCreate, user_id: int) -> Note:
    note_obj = Note(**note.model_dump(), author_id= user_id)
    db.add(note_obj)
    await db.flush()
    await db.refresh(note_obj)

    return note_obj


async def update_note(
        db: AsyncSession,
        note_id: int,
        note: NoteUpdate) -> Note | None:
    note_obj = await get_note_by_id(db, note_id)

    if note_obj is None:
        return None

    update_data = note.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(note_obj, field, value)

    await db.flush()
    await db.refresh(note_obj)

    return note_obj


async def delete_note(db: AsyncSession, note_id: int) -> Note | None:
    note_obj = await get_note_by_id(db, note_id)

    if note_obj is None:
        return None

    await db.delete(note_obj)
    await db.flush()

    return note_obj