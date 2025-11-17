from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.like import Like
from app.models.post import Post
from app.models.thread import Thread
from app.models.user import User
from app.schemas.user import UserUpdate


def get_user_by_id(db: Session, user_id):
    return db.get(User, user_id)


def update_user_profile(db: Session, user: User, payload: UserUpdate) -> User:
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_activity(db: Session, user_id):
    threads_started = db.query(func.count(Thread.id)).filter(Thread.user_id == user_id).scalar() or 0
    posts_written = db.query(func.count(Post.id)).filter(Post.user_id == user_id).scalar() or 0
    likes_given = db.query(func.count(Like.id)).filter(Like.user_id == user_id).scalar() or 0
    return {
        "threads_started": threads_started,
        "posts_written": posts_written,
        "likes_given": likes_given,
    }


def set_user_status(db: Session, user: User, *, is_active: bool | None = None, role: str | None = None) -> User:
    if is_active is not None:
        user.is_active = is_active
    if role == "admin":
        user.is_admin = True
    if role == "moderator":
        user.is_moderator = True
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
