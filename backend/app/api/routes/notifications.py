from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_db
from app.models.notification import Notification
from app.schemas.notification import NotificationPublic, NotificationUpdate
from app.services.notifications import list_notifications, mark_notification_read

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.get("/", response_model=List[NotificationPublic])
def get_my_notifications(
    db: Session = Depends(get_db), current_user=Depends(get_current_active_user)
):
    return list_notifications(db, current_user.id)


@router.post("/{notification_id}/read", response_model=NotificationPublic)
def mark_read(
    notification_id: UUID,
    payload: NotificationUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    notification = db.get(Notification, notification_id)
    if not notification or notification.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    return mark_notification_read(db, notification, payload.is_read)
