from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware

from app.api.routes import (
    admin,
    auth,
    categories,
    flags,
    likes,
    notifications,
    posts,
    search,
    threads,
    users,
)
from app.core.config import settings
from app.core.logging import configure_logging
from app.middleware.rate_limit import limiter

configure_logging()

app = FastAPI(title=settings.APP_NAME, version="0.1.0", openapi_url=f"{settings.API_V1_STR}/openapi.json")
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(users.router, prefix=settings.API_V1_STR)
app.include_router(categories.router, prefix=settings.API_V1_STR)
app.include_router(threads.router, prefix=settings.API_V1_STR)
app.include_router(posts.router, prefix=settings.API_V1_STR)
app.include_router(likes.router, prefix=settings.API_V1_STR)
app.include_router(notifications.router, prefix=settings.API_V1_STR)
app.include_router(flags.router, prefix=settings.API_V1_STR)
app.include_router(search.router, prefix=settings.API_V1_STR)
app.include_router(admin.router, prefix=settings.API_V1_STR)


@app.get("/")
def healthcheck():
    return {"status": "ok"}
