from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_db
from app.models.thread import Thread
from app.schemas.thread import ThreadCreate, ThreadPublic, ThreadUpdate
from app.services import forum as forum_service

router = APIRouter(prefix="/threads", tags=["threads"])


@router.get("/", response_model=List[ThreadPublic])
def list_threads(category_id: UUID | None = None, limit: int = 20, db: Session = Depends(get_db)):
    return forum_service.list_threads(db, category_id, limit)


@router.get("/{thread_id}", response_model=ThreadPublic)
def get_thread(thread_id: UUID, db: Session = Depends(get_db)):
    return forum_service.get_thread(db, thread_id)


@router.post("/", response_model=ThreadPublic, status_code=status.HTTP_201_CREATED)
def create_thread(
    payload: ThreadCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    return forum_service.create_thread(db=db, payload=payload, user_id=current_user.id)


@router.put("/{thread_id}", response_model=ThreadPublic)
def update_thread(
    thread_id: UUID,
    payload: ThreadUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    thread = db.get(Thread, thread_id)
    if not thread:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thread not found")
    if thread.user_id != current_user.id and not current_user.is_moderator:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot edit thread")
    return forum_service.update_thread(db=db, thread=thread, payload=payload)
