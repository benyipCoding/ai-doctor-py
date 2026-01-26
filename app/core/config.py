from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    gemini_base_url: str

    class Config:
        env_file = ".env"


settings = Settings()
