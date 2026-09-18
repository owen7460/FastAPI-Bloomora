from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from config.db_conf import get_db
from schemas.users import UserCreate, UserResponse
from schemas.auth import LoginRequest, TokenResponse
from services.auth import register_user, DuplicateEmailError, login_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await register_user(db, user)

    except DuplicateEmailError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(login_data: LoginRequest, db: AsyncSession = Depends(get_db)):
    token = await login_user(db, login_data.email, login_data.password)

    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    return token
