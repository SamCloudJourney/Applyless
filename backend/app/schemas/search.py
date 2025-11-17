from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class SearchFilters(BaseModel):
    query: str
    category_id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    thread_id: Optional[UUID] = None
    limit: int = 20


class SearchResult(BaseModel):
    id: UUID
    type: str
    title: str
    excerpt: str
    category_id: Optional[UUID]
    thread_id: Optional[UUID]
    created_at: datetime


class SearchResponse(BaseModel):
    total: int
    results: List[SearchResult]
