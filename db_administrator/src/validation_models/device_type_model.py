from pydantic import BaseModel


class BaseDeviceTypeIn(BaseModel):
    description: str
    unit: str


class DeviceTypeIn(BaseDeviceTypeIn):
    super(BaseDeviceTypeIn)
    name: str
