import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(120), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    slug = Column(String(120), unique=True, nullable=False, index=True)
    ordering = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
