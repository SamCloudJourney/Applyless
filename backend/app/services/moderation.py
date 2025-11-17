from sqlalchemy.orm import Session

from app.models.flag import Flag
from app.models.post import Post
from app.schemas.flag import FlagCreate, FlagUpdate


def create_flag(db: Session, *, payload: FlagCreate, user_id):
    flag = Flag(post_id=payload.post_id, reason=payload.reason, user_id=user_id)
    db.add(flag)
    db.commit()
    db.refresh(flag)
    return flag


def list_flags(db: Session, *, status: str | None = None):
    query = db.query(Flag)
    if status:
        query = query.filter(Flag.status == status)
    return query.order_by(Flag.created_at.desc()).all()


def update_flag(db: Session, flag: Flag, payload: FlagUpdate):
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(flag, k, v)
    db.add(flag)
    db.commit()
    db.refresh(flag)
    return flag


def remove_post(db: Session, post: Post):
    db.delete(post)
    db.commit()
