from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from dependencies.auth import get_current_user
from models.users import User
from schemas.announcements import (
    AnnouncementCreate,
    AnnouncementUpdate,
)
from crud import announcements

router = APIRouter(
    prefix="/api/announcements",
    tags=["announcements"],
)


@router.get("/{announcement_id}")
async def get_announcement_by_id(
    announcement_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    announcement_data = await announcements.get_announcement_by_id(db, announcement_id)

    if announcement_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Announcement not found"
        )

    return {
        "code": 200,
        "message": "get announcement successfully",
        "data": announcement_data,
    }


@router.get("/")
async def get_announcements(
    db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)
):
    announcement_data = await announcements.get_announcements(db)

    return {
        "code": 200,
        "message": "get announcements successfully",
        "data": announcement_data,
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_announcement(
    announcement: AnnouncementCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    announcement_data = await announcements.create_announcement(
        db, announcement, created_by=current_user.id
    )

    return {
        "code": 201,
        "message": "create announcement successfully",
        "data": announcement_data,
    }


@router.patch("/{announcement_id}")
async def update_announcement(
    announcement_id: int,
    announcement: AnnouncementUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    updated_announcement = await announcements.update_announcement(
        db,
        announcement_id,
        announcement,
    )

    if updated_announcement is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Announcement not found"
        )

    return {
        "code": 200,
        "message": "update announcement successfully",
        "data": updated_announcement,
    }


@router.delete("/{announcement_id}")
async def delete_announcement(
    announcement_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted_announcement = await announcements.delete_announcement(db, announcement_id)

    if deleted_announcement is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Announcement not found"
        )

    return {
        "code": 200,
        "message": "delete announcement successfully",
        "data": deleted_announcement,
    }
