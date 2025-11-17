from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_db
from app.core.security import decode_token
from app.schemas import auth as auth_schema
from app.schemas.user import UserCreate, UserPublic
from app.services import auth as auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    user = auth_service.register_user(db=db, email=payload.email, username=payload.username, password=payload.password)
    return user


@router.post("/login", response_model=auth_schema.AuthResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_service.authenticate_user(db=db, email=form_data.username, password=form_data.password)
    access_token, refresh_token, expires_at = auth_service.issue_tokens(user.id)
    return auth_schema.AuthResponse(
        user_id=user.id,
        email=user.email,
        username=user.username,
        access_token=access_token,
        refresh_token=refresh_token,
        expires_at=expires_at,
    )


@router.get("/me", response_model=UserPublic)
def read_me(current_user=Depends(get_current_active_user)):
    return current_user


@router.post("/refresh", response_model=auth_schema.Token)
def refresh_token(token_payload: auth_schema.Token):
    if not token_payload.refresh_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing refresh token")
    payload = decode_token(token_payload.refresh_token)
    if payload.get("type") != "refresh":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid refresh token")
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid refresh token")
    access_token, refresh_token, _ = auth_service.issue_tokens(UUID(user_id))
    return auth_schema.Token(access_token=access_token, refresh_token=refresh_token)
