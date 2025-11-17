import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Thread(Base):
    __tablename__ = "threads"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))
    title = Column(String(255), nullable=False)
    tags = Column(String(255), nullable=True)
    trusted_score = Column(Numeric(4, 2), default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("Category", backref="threads")
    author = relationship("User")
