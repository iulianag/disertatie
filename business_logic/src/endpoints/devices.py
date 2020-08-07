from fastapi import APIRouter, Query, Security
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
import requests

from settings import DB_SERVER_URL
from src.utils.base_utils import raise_exception
from src.validation_models.device_model import DeviceIn, BaseDeviceIn


router = APIRouter()


@router.get("/devices",
            tags=["devices"])
async def get_devices(query: str = Query(None),
                      type_name: str = Query(None),
                      authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.get(
            f"{DB_SERVER_URL}/devices",
            headers={"Authorization": authorization},
            params={'query': query,
                    'type_name': type_name}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.post("/devices",
             tags=["devices"])
async def post_device(item: DeviceIn,
                      authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.post(
            f"{DB_SERVER_URL}/devices",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.get("/devices/{id}",
            tags=["devices"])
async def get_device(id: int,
                     authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.get(
            f"{DB_SERVER_URL}/devices/{id}",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/devices/{id}",
               tags=["devices"])
async def delete_device(id: int,
                        authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.delete(
            f"{DB_SERVER_URL}/devices/{id}",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.put("/devices/{id}",
            tags=["devices"])
async def put_device(id: int,
                     item: BaseDeviceIn,
                     authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.put(
            f"{DB_SERVER_URL}/devices/{id}",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)
