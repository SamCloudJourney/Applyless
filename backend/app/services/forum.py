from typing import List
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.category import Category
from app.models.like import Like
from app.models.post import Post
from app.models.thread import Thread
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.schemas.post import PostCreate, PostUpdate
from app.schemas.thread import ThreadCreate, ThreadUpdate


def list_categories(db: Session) -> List[Category]:
    return db.query(Category).order_by(Category.ordering).all()


def create_category(db: Session, payload: CategoryCreate) -> Category:
    category = Category(**payload.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update_category(db: Session, category: Category, payload: CategoryUpdate) -> Category:
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(category, k, v)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category: Category) -> None:
    db.delete(category)
    db.commit()


def list_threads(db: Session, category_id: UUID | None = None, limit: int = 20):
    query = db.query(Thread).order_by(Thread.created_at.desc())
    if category_id:
        query = query.filter(Thread.category_id == category_id)
    return query.limit(limit).all()


def get_thread(db: Session, thread_id: UUID) -> Thread:
    thread = db.get(Thread, thread_id)
    if not thread:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thread not found")
    return thread


def create_thread(db: Session, *, payload: ThreadCreate, user_id: UUID) -> Thread:
    thread = Thread(**payload.model_dump(), user_id=user_id)
    db.add(thread)
    db.commit()
    db.refresh(thread)
    return thread


def update_thread(db: Session, *, thread: Thread, payload: ThreadUpdate) -> Thread:
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(thread, k, v)
    db.add(thread)
    db.commit()
    db.refresh(thread)
    return thread


def list_posts(db: Session, thread_id: UUID) -> List[Post]:
    return (
        db.query(Post)
        .filter(Post.thread_id == thread_id)
        .order_by(Post.created_at.asc())
        .all()
    )


def create_post(db: Session, *, payload: PostCreate, user_id: UUID) -> Post:
    post = Post(**payload.model_dump(), user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def update_post(db: Session, *, post: Post, payload: PostUpdate) -> Post:
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(post, k, v)
    post.is_edited = True
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post: Post) -> None:
    db.delete(post)
    db.commit()


def toggle_like(db: Session, *, post_id: UUID, user_id: UUID) -> dict[str, int]:
    existing = db.query(Like).filter(Like.post_id == post_id, Like.user_id == user_id).first()
    if existing:
        db.delete(existing)
        db.commit()
    else:
        like = Like(post_id=post_id, user_id=user_id)
        db.add(like)
        db.commit()
    total = db.query(func.count(Like.id)).filter(Like.post_id == post_id).scalar() or 0
    return {"likes": total}
