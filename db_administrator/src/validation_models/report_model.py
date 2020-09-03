from pydantic import BaseModel
from typing import List
from datetime import datetime


class AlertModel(BaseModel):
    device_id: int
    name: str
    limit: float
    current_value: float
    alert_date: datetime = None


class AlertListIn(BaseModel):
    data: List[AlertModel] = []
