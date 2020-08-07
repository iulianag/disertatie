from fastapi import APIRouter, Query, Security
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
import requests

from settings import DB_SERVER_URL
from src.utils.base_utils import raise_exception
from src.validation_models.group_model import BaseGroupIn, GroupIn
from src.utils.group_utils import get_group_devices, get_group_profiles

router = APIRouter()


@router.get("/groups",
            tags=["groups"])
async def get_groups(query: str = Query(None),
                     authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.get(
            f"{DB_SERVER_URL}/groups",
            headers={"Authorization": authorization},
            params={'query': query}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.post("/groups",
             tags=["groups"])
async def post_group(item: GroupIn,
                     authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.post(
            f"{DB_SERVER_URL}/groups",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.get("/groups/{id}",
            tags=["groups"])
async def get_group(id: int,
                    authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response1 = requests.get(
            f"{DB_SERVER_URL}/groups/{id}",
            headers={"Authorization": authorization}
        )
        user_details = response1.json()
        if len(user_details['data']) > 0:
            response2 = requests.get(
                f"{DB_SERVER_URL}/groups/{id}/profiles",
                headers={"Authorization": authorization}
            )
            profiles = response2.json()
            user_details['data'][0]['profiles'] = get_group_profiles(profiles['data'])

            response3 = requests.get(
                f"{DB_SERVER_URL}/groups/{id}/devices",
                headers={"Authorization": authorization}
            )
            devices = response3.json()
            user_details['data'][0]['devices'] = get_group_devices(devices['data'])
        return JSONResponse(
            status_code=response1.status_code,
            content=user_details
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/groups/{id}",
               tags=["groups"])
async def delete_group(id: int,
                       authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.delete(
            f"{DB_SERVER_URL}/groups/{id}",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.put("/groups/{id}",
            tags=["groups"])
async def put_group(id: int,
                    item: BaseGroupIn,
                    authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.put(
            f"{DB_SERVER_URL}/groups/{id}",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)