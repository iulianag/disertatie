from pydantic import BaseModel
from typing import List


class AlertModel(BaseModel):
    device_id: int
    parameter: str
    limit: float
    value: float


class AlertListIn(BaseModel):
    data: List[AlertModel] = []
