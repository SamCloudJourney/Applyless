from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.schemas.user import UserPublic


class PostBase(BaseModel):
    content: str


class PostCreate(PostBase):
    thread_id: UUID


class PostUpdate(BaseModel):
    content: Optional[str] = None


class PostPublic(PostBase):
    id: UUID
    thread_id: UUID
    user_id: Optional[UUID]
    is_edited: bool
    created_at: datetime
    updated_at: datetime
    author: Optional[UserPublic]

    class Config:
        from_attributes = True
