from typing import Optional

from fastapi_users import schemas
from pydantic import ConfigDict, EmailStr
from pydantic_core import core_schema
from pydantic_extra_types.phone_numbers import PhoneNumber


class PhoneNumberValidator(PhoneNumber):
    @classmethod
    def _validate(cls, phone_number: str, _: core_schema.ValidationInfo) -> str:
        formatted_number = super()._validate(phone_number, _)
        return formatted_number[4:]


class SchUserRead(schemas.BaseUser[int]):
    id: int
    name: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    telegram_number: Optional[PhoneNumberValidator] = None

    model_config = ConfigDict(from_attributes=True)


class SchUserCreate(schemas.BaseUserCreate):
    email: EmailStr
    name: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    telegram_number: Optional[PhoneNumberValidator] = None

    model_config = ConfigDict(from_attributes=True)


class SchUserUpdate(schemas.BaseUserUpdate):
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None
    telegram_number: Optional[PhoneNumberValidator] = None
