from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Project Ops"
    APP_VERSION: str = "0.1.0"
    ENV: Literal["local", "dev", "staging", "prod"] = "local"

    # Infra
    DATABASE_URL: str = "postgresql+psycopg://app:app@localhost:5432/app"
    REDIS_URL: str = "redis://localhost:6379/0"

    # Logging
    LOG_LEVEL: str = Field(default="INFO")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=True,
    )


settings = Settings()
