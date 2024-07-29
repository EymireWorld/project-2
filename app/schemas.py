from datetime import datetime
from enum import IntEnum

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Schema(BaseModel):
    model_config = ConfigDict(from_attributes= True)


class Scope(IntEnum):
    system = 0
    admin = 1
    user = 2


class TokenSchema(Schema):
    access_token: str
    token_type: str


class UserSchema(Schema):
    id: int
    name: str = Field(min_length=4, max_length=16)
    first_name: str = Field(max_length=16)
    last_name: str = Field(max_length=16)
    email: EmailStr
    hashed_password: bytes
    scope: Scope
    created_at: datetime


class UserShowSchema(Schema):
    id: int
    name: str = Field(min_length=4, max_length=16)
    first_name: str = Field(max_length=16)
    last_name: str = Field(max_length=16)
    email: EmailStr
    scope: Scope
    created_at: datetime


class UserSingUpSchema(Schema):
    name: str = Field(min_length=4, max_length=16)
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)


class UserSingInSchema(Schema):
    name: str = Field(min_length=4, max_length=16)
    password: str = Field(min_length=8, max_length=64)
