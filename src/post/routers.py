from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import SchPostInfo, SchSearchArgsPost, SchSearchArgsAllPost, SchCreatePost, SchUpdatePost
from .manager import PostManager
from .utils import convert_post_info_form
from .exceptions import PostException

from src.core.database import get_async_session
from src.auth.base_config import current_user, current_superuser
from src.auth.models import User

router = APIRouter(
    prefix="/posts",
    tags=["Post"]
)


@router.get('/all', response_model=list[SchPostInfo])
async def get_posts(
        session: AsyncSession = Depends(get_async_session),
        search_args: SchSearchArgsAllPost = Depends()
):
    posts = await PostManager.get_all_posts(session, params=search_args)
    return [convert_post_info_form(post, user) for post, user in posts]


@router.get('', response_model=list[SchPostInfo])
async def get_posts_by_current_user(
        session: AsyncSession = Depends(get_async_session),
        user=Depends(current_user),
        search_args: SchSearchArgsPost = Depends()
):
    posts = await PostManager.get_posts_by_user(session, user, params=search_args)
    return [convert_post_info_form(post, user) for post, user in posts]


@router.post('', response_model=SchPostInfo)
async def add_post(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
        data: SchCreatePost = Depends()
):
    try:
        post, user = await PostManager.add_post(session, user, data)
        return convert_post_info_form(post, user)
    except Exception as _:
        raise PostException.invalid_data()


@router.put('', response_model=SchPostInfo)
async def update_post(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
        data: SchUpdatePost = Depends()
):
    try:
        post = await PostManager.update_post(session, data)
        return convert_post_info_form(post, user)
    except ValueError:
        raise PostException.not_found()
    except Exception as _:
        raise PostException.invalid_data()


@router.delete('/{id}')
async def delete_post(
        post_id: int,
        session: AsyncSession = Depends(get_async_session),
        _: User = Depends(current_superuser),
):
    if await PostManager.delete_post(session, post_id):
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise PostException.not_found()
