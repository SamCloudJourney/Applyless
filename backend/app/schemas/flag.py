from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class FlagCreate(BaseModel):
    post_id: UUID
    reason: str


class FlagPublic(BaseModel):
    id: UUID
    post_id: UUID
    user_id: UUID
    reason: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class FlagUpdate(BaseModel):
    status: Optional[str] = None
