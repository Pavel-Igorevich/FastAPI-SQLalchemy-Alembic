from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, DateTime, func, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


class User(SQLAlchemyBaseUserTable, Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    telegram_number: Mapped[str] = mapped_column(String(length=50), nullable=True)

    posts = relationship("Post", back_populates="author")
