from sqlalchemy import Column, Integer, DateTime, func, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from src.core.database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    header = Column(String, index=True)
    text = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    active = Column(Boolean, index=True, default=True)

    author = relationship("User", back_populates="posts")
