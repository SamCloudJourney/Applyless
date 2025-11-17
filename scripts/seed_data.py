"""Seed initial categories and demo user."""

import uuid

from app.db.session import SessionLocal
from app.models.category import Category
from app.models.user import User
from app.core.security import get_password_hash

CATEGORIES = [
    ("Local Events", "Happenings around East Dulwich"),
    ("Recommendations", "Trusted local services"),
    ("Lost & Found", "Help reunite items"),
    ("Trades", "Plumbers, electricians, tutors"),
]


def run() -> None:
    db = SessionLocal()
    try:
        for name, description in CATEGORIES:
            if not db.query(Category).filter(Category.slug == name.lower().replace(" ", "-")).first():
                category = Category(
                    name=name,
                    description=description,
                    slug=name.lower().replace(" ", "-"),
                )
                db.add(category)
        if not db.query(User).filter(User.email == "demo@eastdulwich.local").first():
            db.add(
                User(
                    email="demo@eastdulwich.local",
                    username="se22demo",
                    password_hash=get_password_hash("password123"),
                    badges="trusted-local",
                )
            )
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    run()
