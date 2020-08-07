from pydantic import BaseModel


class BaseDeviceIn(BaseModel):
    description: str
    limit: float


class DeviceIn(BaseDeviceIn):
    super(BaseDeviceIn)
    name: str
    type_id: int
