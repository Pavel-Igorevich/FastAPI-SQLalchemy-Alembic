from sqlalchemy import Column, Integer, DateTime, func, String, ForeignKey, Boolean, event
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from src.core.database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    update_time = Column(DateTime(timezone=True), onupdate=func.now())
    header = Column(String, index=True)
    text = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    active = Column(Boolean, index=True, default=True)

    author = relationship("User", back_populates="posts")


@event.listens_for(Post, 'before_insert')
def before_insert(_, connection, target):
    current_time = connection.execute(expression.select(func.now())).scalar()
    target.update_time = target.created_time = current_time
