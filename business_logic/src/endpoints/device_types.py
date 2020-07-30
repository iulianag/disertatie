from fastapi import APIRouter, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.validation_models.device_type_model import DeviceTypeIn, BaseDeviceTypeIn
from src.utils.base_utils import raise_exception


router = APIRouter()


@router.get("/types",
            tags=["types"])
async def get_types(query: str = Query(None)):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.post("/types",
             tags=["types"])
async def post_type(item: DeviceTypeIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.get("/types/{type_id}",
            tags=["types"])
async def get_type(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.delete("/types/{type_id}",
               tags=["types"])
async def delete_type(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.put("/types/{type_id}",
            tags=["types"])
async def put_type(id: int, item: BaseDeviceTypeIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)