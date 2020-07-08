from pydantic import BaseModel


class BaseGroupIn(BaseModel):
    description: str


class GroupIn(BaseGroupIn):
    super(BaseGroupIn)
    name: str
