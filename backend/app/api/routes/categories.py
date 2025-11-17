from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin, get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryPublic, CategoryUpdate
from app.services import forum as forum_service

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=List[CategoryPublic])
def list_categories(db: Session = Depends(get_db)):
    return forum_service.list_categories(db)


@router.get("/{category_id}", response_model=CategoryPublic)
def read_category(category_id: UUID, db: Session = Depends(get_db)):
    category = db.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return category


@router.post("/", response_model=CategoryPublic, status_code=status.HTTP_201_CREATED)
def create_category(
    payload: CategoryCreate,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_admin),
):
    return forum_service.create_category(db, payload)


@router.put("/{category_id}", response_model=CategoryPublic)
def update_category(
    category_id: UUID,
    payload: CategoryUpdate,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_admin),
):
    category = db.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    return forum_service.update_category(db, category, payload)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: UUID,
    db: Session = Depends(get_db),
    _: str = Depends(get_current_admin),
):
    category = db.get(Category, category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    forum_service.delete_category(db, category)
    return {"status": "deleted"}
