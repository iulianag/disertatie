from pydantic import BaseModel
from datetime import datetime


class AlertModel(BaseModel):
    device_id: int
    name: str
    limit: float
    current_value: float
    alert_date: datetime = None


class ReportModel(BaseModel):
    device_id: int
    name: str
    current_value: float
    report_date: datetime = None
