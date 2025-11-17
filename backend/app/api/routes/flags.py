from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_current_admin, get_db
from app.models.flag import Flag
from app.schemas.flag import FlagCreate, FlagPublic, FlagUpdate
from app.services import moderation as moderation_service

router = APIRouter(prefix="/flags", tags=["flags"])


@router.post("/", response_model=FlagPublic, status_code=status.HTTP_201_CREATED)
def create_flag(
    payload: FlagCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    return moderation_service.create_flag(db=db, payload=payload, user_id=current_user.id)


@router.get("/", response_model=List[FlagPublic])
def list_flags(
    status_filter: str | None = None,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_admin),
):
    return moderation_service.list_flags(db=db, status=status_filter)


@router.patch("/{flag_id}", response_model=FlagPublic)
def update_flag(
    flag_id: UUID,
    payload: FlagUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_admin),
):
    flag = db.get(Flag, flag_id)
    if not flag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Flag not found")
    return moderation_service.update_flag(db=db, flag=flag, payload=payload)
