from fastapi import APIRouter, Query, Security
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
import requests

from settings import DB_SERVER_URL
from src.validation_models.device_type_model import DeviceTypeIn, BaseDeviceTypeIn
from src.utils.base_utils import raise_exception
from src.utils.type_utils import get_type_devices


router = APIRouter()


@router.get("/types",
            tags=["types"])
async def get_types(query: str = Query(None),
                    authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.get(
            f"{DB_SERVER_URL}/types",
            headers={"Authorization": authorization},
            params={'query': query}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.post("/types",
             tags=["types"])
async def post_type(item: DeviceTypeIn,
                    authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.post(
            f"{DB_SERVER_URL}/types",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.get("/types/{id}",
            tags=["types"])
async def get_type(id: int,
                   authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response1 = requests.get(
            f"{DB_SERVER_URL}/types/{id}",
            headers={"Authorization": authorization}
        )
        type_details = response1.json()
        if len(type_details['data']) > 0:
            response2 = requests.get(
                f"{DB_SERVER_URL}/devices",
                headers={"Authorization": authorization},
                params={'type_name': type_details['data'][0]['name']}
            )
            devices = response2.json()
            type_details['data'][0]['devices'] = get_type_devices(devices['data'])
        return JSONResponse(
            status_code=response1.status_code,
            content=type_details
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/types/{id}",
               tags=["types"])
async def delete_type(id: int,
                      authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.delete(
            f"{DB_SERVER_URL}/types/{id}",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.put("/types/{id}",
            tags=["types"])
async def put_type(id: int,
                   item: BaseDeviceTypeIn,
                   authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.put(
            f"{DB_SERVER_URL}/types/{id}",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)