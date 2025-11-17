from datetime import datetime, timedelta, timezone
from typing import Optional
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import create_access_token, create_refresh_token, get_password_hash, verify_password
from app.models.user import User


def register_user(*, db: Session, email: str, username: str, password: str) -> User:
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    user = User(email=email, username=username, password_hash=get_password_hash(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(*, db: Session, email: str, password: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is banned")
    return user


def issue_tokens(user_id: UUID) -> tuple[str, str, datetime]:
    access_token = create_access_token(str(user_id))
    refresh_token = create_refresh_token(str(user_id))
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=15)
    return access_token, refresh_token, expires_at


def rotate_refresh_token(refresh_token: str) -> str:
    return create_refresh_token(refresh_token)
