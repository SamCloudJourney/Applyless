import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    username = Column(String(64), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    bio = Column(Text, nullable=True)
    avatar_url = Column(String(512), nullable=True)
    location = Column(String(255), nullable=True)
    badges = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    is_moderator = Column(Boolean, default=False)
    trusted_score = Column(String(32), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
