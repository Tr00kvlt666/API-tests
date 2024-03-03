from pydantic import BaseModel, Field

import typing as t


class SupportDataModel(BaseModel):
    url: str = Field(...)
    text: str = Field(...)


class UserDataModel(BaseModel):
    id: int = Field(...)
    email: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    avatar: str = Field(...)


class ListUsersModel(BaseModel):
    page: int = Field(...)
    per_page: int = Field(...)
    total: int = Field(...)
    total_pages: int = Field(...)
    data: t.List[UserDataModel] = Field(...)
    support: SupportDataModel = Field(...)


class SingleUserDataModel(BaseModel):
    data: UserDataModel = Field(...)
    support: SupportDataModel = Field(...)

