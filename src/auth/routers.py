from fastapi import APIRouter
from .base_config import fastapi_users, auth_backend
from .schemas import SchUserCreate, SchUserRead, SchUserUpdate


router = APIRouter()
prefix_auth = "/auth"

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_register_router(SchUserRead, SchUserCreate),
    prefix=prefix_auth,
    tags=["Auth"],
)

# todo продумать работу и регистрацию по почте/ телеграм
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix=prefix_auth,
    tags=["Auth"],
)
# todo разобраться
# router.include_router(
#     fastapi_users.get_verify_router(SchUserRead),
#     prefix=prefix_auth,
#     tags=["Auth"],
# )


router.include_router(
    fastapi_users.get_users_router(SchUserRead, SchUserUpdate),
    prefix="/users",
    tags=["Users"],
)

