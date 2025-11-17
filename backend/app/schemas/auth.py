from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str | None = None
    exp: int | None = None
    type: str | None = None


class AuthResponse(BaseModel):
    user_id: UUID
    email: EmailStr
    username: str
    access_token: str
    refresh_token: str
    expires_at: datetime
