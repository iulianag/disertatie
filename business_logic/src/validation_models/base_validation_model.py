from pydantic import BaseModel
from typing import List


class InfoModel(BaseModel):
    type: str
    message: str


class BaseResponseModel(BaseModel):
    meta: dict = {}
    info: List[InfoModel] = []
    data: List[dict] = []
