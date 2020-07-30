from fastapi import APIRouter, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.utils.base_utils import raise_exception
from src.validation_models.device_model import DeviceIn, BaseDeviceIn
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


router = APIRouter()


@router.get("/devices",
            tags=["devices"])
async def get_devices(query: str = Query(None), type_name: str = Query(None)):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.post("/devices",
             tags=["devices"])
async def post_device(item: DeviceIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.get("/devices/{device_id}",
            tags=["devices"])
async def get_device(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.delete("/devices/{device_id}",
               tags=["devices"])
async def delete_device(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.put("/devices/{device_id}",
            tags=["devices"])
async def put_device(id: int, item: BaseDeviceIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)
