import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Flag(Base):
    __tablename__ = "flags"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"))
    reason = Column(String(255), nullable=False)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
