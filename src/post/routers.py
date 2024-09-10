from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Post, CreatePost, UpdatePost, SearchArgsPost, SearchArgsAllPost
from .manager import orm_get_posts
from src.core.database import get_async_session
from src.auth.base_config import current_user

from icecream import ic

router = APIRouter(
    prefix="/posts",
    tags=["Post"]
)


@router.get('/all', response_model=list[Post])
async def get_posts(
        session: AsyncSession = Depends(get_async_session),
        search_args: SearchArgsAllPost = Depends()
) -> list[Post]:
    posts = await orm_get_posts(session, limit=search_args.limit, offset=search_args.offset)
    return [
        Post(
            id=post.id,
            created_time=post.created_time,
            update_time=post.update_time,
            header=post.header,
            text=post.text,
            author_name=user.name,
            email=user.email,
            telegram=user.telegram_number
        )
        for post, user in posts
    ]


@router.post('')
def add_post(data: CreatePost, session: AsyncSession = Depends(get_async_session), user=Depends(current_user)):
    return user


@router.patch('')
def update_post(data: UpdatePost, session: AsyncSession = Depends(get_async_session), user=Depends(current_user)):
    return user


@router.get('')
async def get_my_posts(
        session: AsyncSession = Depends(get_async_session),
        user=Depends(current_user),
        search_args: SearchArgsPost = Depends()
):
    return []
