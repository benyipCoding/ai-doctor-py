from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    gemini_base_url: str
    # PostgreSQL connection string, e.g. postgresql+asyncpg://user:pass@host:port/dbname
    database_url: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
