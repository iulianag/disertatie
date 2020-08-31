from pydantic import BaseModel


class BaseUserIn(BaseModel):
    full_name: str
    email: str


class UserCredentialsIn(BaseModel):
    username: str
    password: str


class UserIn(UserCredentialsIn, BaseUserIn):
    super(UserCredentialsIn)
    super(BaseUserIn)


class UserProfileIn(BaseModel):
    user_id: int
    profile_id: int

