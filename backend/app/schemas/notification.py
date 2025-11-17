from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class NotificationPublic(BaseModel):
    id: UUID
    user_id: UUID
    type: str
    data: Any | None
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True


class NotificationUpdate(BaseModel):
    is_read: bool = True
