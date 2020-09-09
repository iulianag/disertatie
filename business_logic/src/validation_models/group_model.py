from pydantic import BaseModel


class BaseGroupIn(BaseModel):
    description: str


class GroupIn(BaseGroupIn):
    super(BaseGroupIn)
    name: str


class GroupDeviceIn(BaseModel):
    group_id: int
    device_id: int
