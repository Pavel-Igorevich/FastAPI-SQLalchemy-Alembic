from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    SECRET_AUTH: str
    SECRET_ALGORITHM: str

    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}"
            f"/{self.DB_NAME}?async_fallback=True"
        )

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

