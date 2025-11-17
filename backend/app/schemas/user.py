from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    username: str
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    location: Optional[str] = None
    badges: Optional[str] = None


class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=64)
    password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    location: Optional[str] = None
    badges: Optional[str] = None


class UserPublic(UserBase):
    id: UUID
    is_admin: bool
    is_moderator: bool
    is_active: bool
    trusted_score: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class UserActivity(BaseModel):
    threads_started: int
    posts_written: int
    likes_given: int
