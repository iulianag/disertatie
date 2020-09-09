from pydantic import BaseModel


class AlertModel(BaseModel):
    id: int
    parameter: str
    limit: float
    value: float


class ReportModel(BaseModel):
    id: int
    parameter: str
    value: float
