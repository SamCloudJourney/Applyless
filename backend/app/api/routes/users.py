from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_current_admin, get_db
from app.models.user import User
from app.schemas.user import UserActivity, UserPublic, UserUpdate
from app.services import users as user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=List[UserPublic])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.created_at.desc()).all()


@router.get("/{user_id}", response_model=UserPublic)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.patch("/me", response_model=UserPublic)
def update_me(
    payload: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    return user_service.update_user_profile(db=db, user=current_user, payload=payload)


@router.get("/me/activity", response_model=UserActivity)
def get_my_activity(
    current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)
):
    return user_service.get_activity(db=db, user_id=current_user.id)


@router.post("/{user_id}/ban", response_model=UserPublic)
def ban_user(
    user_id: UUID,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_service.set_user_status(db=db, user=user, is_active=False)


@router.post("/{user_id}/promote", response_model=UserPublic)
def promote_user(
    user_id: UUID,
    role: str,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_admin),
):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_service.set_user_status(db=db, user=user, role=role)
