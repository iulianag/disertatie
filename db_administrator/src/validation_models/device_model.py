from pydantic import BaseModel


class BaseDeviceIn(BaseModel):
    description: str
    limit: str


class DeviceIn(BaseDeviceIn):
    super(BaseDeviceIn)
    name: str
    type_id: str
