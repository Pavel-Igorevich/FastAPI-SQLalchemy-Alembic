from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, date
from typing import Optional


class Post(BaseModel):
    id: int
    created_time: datetime
    update_time: Optional[datetime] = None
    header: str
    text: str
    author_name: str
    telegram: Optional[str] = None
    email: str

    model_config = ConfigDict(from_attributes=True)


class SearchArgsPost(BaseModel):
    limit: int = Field(default=10, ge=1)
    offset: int = Field(default=0, ge=0)
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    key: Optional[str] = None


class SearchArgsAllPost(SearchArgsPost):
    author_name: Optional[str] = None


class CreatePost(BaseModel):
    header: str
    text: str

    model_config = ConfigDict(from_attributes=True)


class UpdatePost(BaseModel):
    id: int
    text: Optional[str] = None
    active: bool

    model_config = ConfigDict(from_attributes=True)
