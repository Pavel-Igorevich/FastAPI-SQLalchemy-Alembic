from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import PostInfo, SearchArgsPost, SearchArgsAllPost, CreatePost, UpdatePost
from .manager import PostManager
from .utils import convert_post_info_form
from src.core.database import get_async_session
from src.auth.base_config import current_user
from src.auth.models import User

router = APIRouter(
    prefix="/posts",
    tags=["Post"]
)


@router.get('/all', response_model=list[PostInfo])
async def get_posts(
        session: AsyncSession = Depends(get_async_session),
        search_args: SearchArgsAllPost = Depends()
):
    posts = await PostManager.get_all_posts(session, params=search_args)
    return [convert_post_info_form(post, user) for post, user in posts]


@router.get('', response_model=list[PostInfo])
async def get_posts_by_current_user(
        session: AsyncSession = Depends(get_async_session),
        user=Depends(current_user),
        search_args: SearchArgsPost = Depends()
):
    posts = await PostManager.get_posts_by_user(session, user, params=search_args)
    return [convert_post_info_form(post, user) for post, user in posts]


@router.post('', response_model=PostInfo)
async def add_post(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
        data: CreatePost = Depends()
):
    try:
        post, user = await PostManager.add_post(session, user, data)
        return convert_post_info_form(post, user)
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=400, detail="Invalid data")


@router.put('', response_model=PostInfo)
async def update_post(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
        data: UpdatePost = Depends()
):
    try:
        post = await PostManager.update_post(session, data)
        return convert_post_info_form(post, user)
    except ValueError:
        raise HTTPException(status_code=404, detail="Post not found")
    except Exception as exc:
        print(exc)
        raise HTTPException(status_code=400, detail="Invalid data")


# @router.get('add_test_posts')
# async def add_test_posts(session: AsyncSession = Depends(get_async_session)):
#     return await add_posts_to_existing_users(session)
