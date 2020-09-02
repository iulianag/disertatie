from pydantic import BaseModel
from fastapi import Form


class BaseUserIn(BaseModel):
    full_name: str = Form(...)
    email: str = Form(...)


class UserCredentialsIn(BaseModel):
    username: str = Form(...)
    password: str = Form(...)


class UserIn(UserCredentialsIn, BaseUserIn):
    super(UserCredentialsIn)
    super(BaseUserIn)


class UserProfileIn(BaseModel):
    user_id: int
    profile_id: int

