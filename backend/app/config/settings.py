# backend/app/config/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AgriAssist API"
    env: str = "dev"
    log_level: str = "INFO"

    # Placeholder fields for when we wire real services
    # database_url: str | None = None
    # imd_api_key: str | None = None
    # enam_api_key: str | None = None

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
