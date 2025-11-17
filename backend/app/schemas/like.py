from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class LikePublic(BaseModel):
    id: UUID
    post_id: UUID
    user_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
