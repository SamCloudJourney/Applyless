from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin, get_db
from app.models.flag import Flag
from app.models.post import Post
from app.models.thread import Thread
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[Depends(get_current_admin)])


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    return {
        "users": db.query(func.count(User.id)).scalar() or 0,
        "threads": db.query(func.count(Thread.id)).scalar() or 0,
        "posts": db.query(func.count(Post.id)).scalar() or 0,
        "flags_pending": db.query(func.count(Flag.id)).filter(Flag.status == "pending").scalar() or 0,
    }
