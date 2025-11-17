from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_db
from app.services import forum as forum_service

router = APIRouter(prefix="/likes", tags=["likes"])


@router.post("/{post_id}")
def toggle_like(
    post_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    return forum_service.toggle_like(db=db, post_id=post_id, user_id=current_user.id)
