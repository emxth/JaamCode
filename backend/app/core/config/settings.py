from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Project Ops"
    APP_VERSION: str = "0.1.0"
    ENV: str = "local"

    DATABASE_URL: str = "postgresql+psycopg://app:app@localhost:5432/app"

    REDIS_URL: str = "redis://localhost:6379/0"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()