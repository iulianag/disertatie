from pydantic import BaseModel


class BaseUserIn(BaseModel):
    full_name: str
    email: str


class UserIn(BaseUserIn):
    super(BaseUserIn)
    username: str
    password: str
