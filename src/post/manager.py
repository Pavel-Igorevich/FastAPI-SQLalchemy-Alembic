from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from .models import Post


async def orm_get_posts(session: AsyncSession, limit: int, offset: int) -> list[tuple[Post, User]]:
    query = select(
        Post, User
    ).join(
        User, Post.author_id == User.id
    ).where(Post.active).order_by(Post.id).limit(limit).offset(offset)

    result = await session.execute(query)
    return result.fetchall()
