from typing import Optional

from fastapi import Depends, Request

from fastapi_users import BaseUserManager, IntegerIDMixin

from src.auth.models import User
from src.core.config import settings
from .utils import get_user_db


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.USER_SECRET_KEY
    verification_token_secret = settings.USER_SECRET_KEY


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
