from datetime import date, timedelta
from typing import Optional, Union

from sqlalchemy import select, or_, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from .models import Post
from .schemas import SearchArgsAllPost, SearchArgsPost, CreatePost, UpdatePost


class PostManager:

    @staticmethod
    async def get_posts(
            session: AsyncSession,
            params: Union[SearchArgsPost, SearchArgsAllPost],
            author_id: Optional[int] = None
    ) -> list[tuple[Post, User]]:
        query = select(Post, User).join(User, Post.author_id == User.id)
        if author_id:
            query = query.where(Post.author_id == author_id)

        if params.active is not None:
            query = query.where(Post.active == params.active)

        if isinstance(params, SearchArgsAllPost) and params.author_name:
            query = query.where(User.name.ilike(f"%{params.author_name}%"))

        if params.date_from:
            query = query.where(Post.created_time >= params.date_from)
        if params.date_to:
            query = query.where(Post.created_time <= params.date_to)

        if params.key:
            query = query.where(
                or_(
                    Post.header.ilike(f"%{params.key}%"),
                    Post.text.ilike(f"%{params.key}%")
                )
            )
        query = query.limit(params.limit).offset(params.offset)
        result = await session.execute(query)
        return result.fetchall()

    @staticmethod
    async def get_all_posts(session: AsyncSession, params: SearchArgsAllPost) -> list[tuple[Post, User]]:
        return await PostManager.get_posts(
            session=session,
            params=params
        )

    @staticmethod
    async def get_posts_by_user(
            session: AsyncSession,
            current_user: User,
            params: SearchArgsPost
    ) -> list[tuple[Post, User]]:
        return await PostManager.get_posts(
            session=session,
            params=params,
            author_id=current_user.id
        )

    @staticmethod
    async def add_post(
            session: AsyncSession,
            current_user: User,
            data: CreatePost
    ):
        new_post = Post(
            header=data.header,
            text=data.text,
            author_id=current_user.id
        )
        session.add(new_post)
        await session.commit()
        await session.refresh(new_post)
        return new_post, current_user

    @staticmethod
    async def update_post(
            session: AsyncSession,
            data: UpdatePost
    ) -> Post:
        result = await session.execute(select(Post).filter_by(id=data.id))
        post = result.scalar()
        if not post:
            raise ValueError("Post not found")
        if data.header is not None:
            post.header = data.header
        if data.text is not None:
            post.text = data.text
        if data.active is not None:
            post.active = data.active
        post.update_time = func.now()

        await session.commit()
        await session.refresh(post)
        return post



#
#
# async def orm_get_all_posts(session: AsyncSession, limit: int, offset: int) -> list[tuple[Post, User]]:
#     query = select(
#         Post, User
#     ).join(
#         User, Post.author_id == User.id
#     ).where(Post.active).order_by(Post.id).limit(limit).offset(offset)
#
#     result = await session.execute(query)
#     return result.fetchall()


# async def orm_get_posts(
#         session: AsyncSession,
#         limit: int,
#         offset: int,
#         date_from: Optional[date] = None,
#         date_to: Optional[date] = None,
#         key: Optional[str] = None,
#         author_name: Optional[str] = None
# ) -> list[tuple[Post, User]]:
#     query = select(Post, User).join(User, Post.author_id == User.id).where(Post.active)
#
#     if author_name:
#         query = query.where(User.name.ilike(f"%{author_name}%"))
#
#     # Фильтр по дате создания
#     if date_from:
#         query = query.where(Post.created_time >= date_from)
#     if date_to:
#         query = query.where(Post.created_time <= date_to)
#
#     # Фильтр по ключевому слову (например, ищем в заголовке или тексте)
#     if key:
#         query = query.where(
#             or_(
#                 Post.header.ilike(f"%{key}%"),
#                 Post.text.ilike(f"%{key}%")
#             )
#         )
#
#     query = query.order_by(Post.id).limit(limit).offset(offset)
#
#     result = await session.execute(query)
#     return result.fetchall()
#
#
# async def add_post(session: AsyncSession, data: Post) -> Post:
#     try:
#         post = Post(
#
#         )
#         session.add(post)
#         await session.commit()
#         return post
#     except SQLAlchemyError as exc:
#         await session.rollback()
#         print(f"Error adding post - {exc}")


async def add_posts_to_existing_users(session):
    user_ids = [1, 2, 3]

    # Начальная дата, с которой будут генерироваться посты

    # Добавляем по 10 постов для каждого пользователя
    for user_id in user_ids:
        posts = [
            Post(
                header=f"Post {i} by user {user_id}",
                text=f"This is the content of post {i} by user {user_id}.",
                author_id=user_id,
                active=True
            )
            for i in range(1, 11)
        ]
        session.add_all(posts)

    # Сохраняем посты
    await session.commit()
