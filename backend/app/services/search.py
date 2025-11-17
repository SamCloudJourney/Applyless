from sqlalchemy import func, text
from sqlalchemy.orm import Session

from app.models.post import Post
from app.models.thread import Thread
from app.schemas.search import SearchFilters, SearchResponse, SearchResult


def search_forum(db: Session, filters: SearchFilters) -> SearchResponse:
    query_text = f"%{filters.query.lower()}%"

    thread_query = (
        db.query(
            Thread.id.label("id"),
            Thread.title.label("title"),
            Thread.created_at.label("created_at"),
            Thread.category_id.label("category_id"),
            Thread.id.label("thread_id"),
            func.substr(Thread.title, 1, 200).label("excerpt"),
        )
        .filter(func.lower(Thread.title).like(query_text))
    )
    if filters.category_id:
        thread_query = thread_query.filter(Thread.category_id == filters.category_id)

    post_query = (
        db.query(
            Post.id.label("id"),
            Post.content.label("title"),
            Post.created_at.label("created_at"),
            Post.thread_id.label("thread_id"),
            func.nullif(Post.thread_id, None).label("category_id"),
            func.substr(Post.content, 1, 200).label("excerpt"),
        )
        .filter(func.lower(Post.content).like(query_text))
    )
    if filters.thread_id:
        post_query = post_query.filter(Post.thread_id == filters.thread_id)

    thread_results = [
        SearchResult(
            id=row.id,
            type="thread",
            title=row.title,
            excerpt=row.excerpt,
            category_id=row.category_id,
            thread_id=row.thread_id,
            created_at=row.created_at,
        )
        for row in thread_query.limit(filters.limit).all()
    ]

    post_results = [
        SearchResult(
            id=row.id,
            type="post",
            title=row.title,
            excerpt=row.excerpt,
            category_id=row.category_id,
            thread_id=row.thread_id,
            created_at=row.created_at,
        )
        for row in post_query.limit(filters.limit).all()
    ]

    results = thread_results + post_results
    return SearchResponse(total=len(results), results=results)
