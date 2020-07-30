from pydantic import BaseModel


class BaseProfileIn(BaseModel):
    description: str


class ProfileIn(BaseProfileIn):
    super(BaseProfileIn)
    name: str
