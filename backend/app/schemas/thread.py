from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.schemas.user import UserPublic


class ThreadBase(BaseModel):
    title: str
    tags: Optional[str] = None


class ThreadCreate(ThreadBase):
    category_id: UUID


class ThreadUpdate(BaseModel):
    title: Optional[str] = None
    tags: Optional[str] = None


class ThreadPublic(ThreadBase):
    id: UUID
    category_id: UUID
    user_id: Optional[UUID]
    trusted_score: float | None = None
    created_at: datetime
    author: Optional[UserPublic] = None

    class Config:
        from_attributes = True
