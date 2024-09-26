from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime, date
from typing import Optional


class PostInfo(BaseModel):
    id: int
    created_time: datetime
    update_time: Optional[datetime] = None
    header: str
    text: str
    author_name: str
    telegram: Optional[str] = None
    email: str
    active: bool

    model_config = ConfigDict(from_attributes=True)


class SearchArgsPost(BaseModel):
    limit: int = Field(default=10, ge=1)
    offset: int = Field(default=0, ge=0)
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    key: Optional[str] = None
    active: Optional[bool] = True


class SearchArgsAllPost(SearchArgsPost):
    author_name: Optional[str] = None


class CreatePost(BaseModel):
    header: str
    text: str


class UpdatePost(BaseModel):
    id: int
    header: Optional[str] = None
    text: Optional[str] = None
    active: bool
