from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    slug: str
    ordering: int = 0


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    ordering: Optional[int] = None


class CategoryPublic(CategoryBase):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
