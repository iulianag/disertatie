from pydantic import BaseModel


class BaseProfileIn(BaseModel):
    description: str


class ProfileIn(BaseProfileIn):
    super(BaseProfileIn)
    name: str


class ProfileGroupIn(BaseModel):
    profile_id: int
    group_id: int
