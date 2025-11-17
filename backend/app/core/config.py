from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    APP_NAME: str = "East Dulwich Forum API"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3
    DATABASE_URL: str
    REDIS_URL: str | None = None
    EMAIL_SENDER: str = "no-reply@eastdulwichforum.com"
    RATE_LIMIT: str = "60/minute"
    ALLOWED_ORIGINS: List[AnyHttpUrl] | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
