from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.search import SearchFilters, SearchResponse
from app.services.search import search_forum

router = APIRouter(prefix="/search", tags=["search"])


@router.post("/", response_model=SearchResponse)
def run_search(filters: SearchFilters, db: Session = Depends(get_db)):
    return search_forum(db, filters)
