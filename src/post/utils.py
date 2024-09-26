from .schemas import PostInfo
from .models import Post
from src.auth.models import User


def convert_post_info_form(post_data: Post, user_data: User) -> PostInfo:
    return PostInfo(
        id=post_data.id,
        created_time=post_data.created_time,
        update_time=post_data.update_time,
        header=post_data.header,
        text=post_data.text,
        author_name=user_data.name,
        email=user_data.email,
        telegram=user_data.telegram_number,
        active=post_data.active
    )
