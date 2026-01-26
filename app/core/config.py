# app/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    gemini_base_url: str

    # async: FastAPI / SQLAlchemy AsyncSession 使用
    database_url_async: str

    # sync: Alembic / CLI / migration 使用
    database_url_sync: str

    class Config:
        env_file = ".env"


settings = Settings()
