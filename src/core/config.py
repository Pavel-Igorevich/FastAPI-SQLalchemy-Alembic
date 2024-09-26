from pydantic_settings import BaseSettings
from pydantic import root_validator
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    SECRET_AUTH: str
    DATABASE_URL: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Вычисляем DATABASE_URL после инициализации объекта
        self.DATABASE_URL = (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}"
            f"/{self.DB_NAME}?async_fallback=True"
        )

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
