from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from dependencies.auth import get_current_user
from models.users import User

from crud import notes
from schemas.notes import NoteCreate, NoteUpdate

router = APIRouter(prefix="/api/notes", tags=["notes"])


@router.get("/{note_id}")
async def get_note_by_id(
    note_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    note_data = await notes.get_note_by_id(db, note_id)

    if note_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)

    return {
        "code": 200,
        "message": "get note successfully",
        "data": note_data,
    }


@router.get("/")
async def get_notes(
    page: int = 1,
    page_size: int = Query(default=25, alias = "pageSize"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    skip = (page - 1) * page_size
    limit = page_size
    note_data = await notes.get_notes(db, skip, limit)

    return {
        "code": 200,
        "message": "get notes successfully",
        "data": note_data,
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(
        note: NoteCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    created_note = await notes.create_note(db, note, current_user.id)

    return {
        "code": 201,
        "message": "create note successfully",
        "data": created_note,
    }


@router.patch("/{note_id}")
async def update_note(
        note_id: int,
        note: NoteUpdate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    updated_note = await notes.update_note(db, note_id, note)

    if updated_note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)

    return {
        "code": 200,
        "message": "update note successfully",
        "data": updated_note,
    }


@router.delete("/{note_id}")
async def delete_note(
        note_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    deleted_note = await notes.delete_note(db, note_id)

    if deleted_note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)

    return {
        "code": 200,
        "message": "delete note successfully",
        "data": deleted_note
    }