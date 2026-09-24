from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from src.post.routers import get_posts

router = APIRouter(
    prefix="/pages",
    tags=['Frontend']
)

templates = Jinja2Templates(directory="./templates")


@router.get('/posts')
async def get_posts_page(
        request: Request,
        posts=Depends(get_posts)
):
    return templates.TemplateResponse(
        name="post/all_posts.html",
        context={'request': request, 'posts': posts},

    )


@router.get('/test')
async def get_posts_page(
        request: Request,
        posts=Depends(get_posts)
):
    return templates.TemplateResponse(
        name="post/index.html",
        context={'request': request, 'posts': posts},

    )