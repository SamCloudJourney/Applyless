from typing import Any, Dict, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.notification import Notification


def create_notification(db: Session, *, user_id: UUID, type_: str, data: Dict[str, Any] | None = None):
    notification = Notification(user_id=user_id, type=type_, data=data and str(data))
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification


def list_notifications(db: Session, user_id: UUID) -> List[Notification]:
    return (
        db.query(Notification)
        .filter(Notification.user_id == user_id)
        .order_by(Notification.created_at.desc())
        .all()
    )


def mark_notification_read(db: Session, notification: Notification, is_read: bool = True) -> Notification:
    notification.is_read = is_read
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification
