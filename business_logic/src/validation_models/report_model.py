from pydantic import BaseModel


class AlertModel(BaseModel):
    device_id: int
    parameter: str
    limit: float
    value: float


class ReportModel(BaseModel):
    device_id: int
    parameter: str
    value: float
