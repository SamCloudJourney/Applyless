from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_active_user, get_db
from app.models.post import Post
from app.schemas.post import PostCreate, PostPublic, PostUpdate
from app.services import forum as forum_service
from app.services.notifications import create_notification

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/thread/{thread_id}", response_model=List[PostPublic])
def list_posts(thread_id: UUID, db: Session = Depends(get_db)):
    return forum_service.list_posts(db, thread_id)


@router.post("/", response_model=PostPublic, status_code=status.HTTP_201_CREATED)
def create_post(
    payload: PostCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    post = forum_service.create_post(db=db, payload=payload, user_id=current_user.id)
    if post.thread.user_id and post.thread.user_id != current_user.id:
        create_notification(
            db,
            user_id=post.thread.user_id,
            type_="reply",
            data={"thread_id": str(post.thread_id), "post_id": str(post.id)},
        )
    return post


@router.put("/{post_id}", response_model=PostPublic)
def update_post(
    post_id: UUID,
    payload: PostUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.user_id != current_user.id and not current_user.is_moderator:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot edit post")
    return forum_service.update_post(db=db, post=post, payload=payload)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    post = db.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    if post.user_id != current_user.id and not current_user.is_moderator:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot delete post")
    forum_service.delete_post(db, post)
    return {"status": "deleted"}
