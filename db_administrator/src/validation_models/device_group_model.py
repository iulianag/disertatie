from pydantic import BaseModel


class DevicegroupIn(BaseModel):
    device_id: int
    group_id: int