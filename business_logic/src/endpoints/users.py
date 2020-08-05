from fastapi import APIRouter, Query, Security
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
import requests

from settings import DB_SERVER_URL
from src.validation_models.user_model import UserIn, BaseUserIn, UserProfileIn
from src.utils.base_utils import raise_exception
from src.utils.user_utils import get_user_profiles

router = APIRouter()


@router.get("/users",
            tags=["Users"])
async def get_users(query: str = Query(None),
                    authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.get(
            f"{DB_SERVER_URL}/users",
            headers={"Authorization": authorization},
            params={'query': query}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.post("/users",
             tags=["Users"])
async def post_user(item: UserIn,
                    authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.post(
            f"{DB_SERVER_URL}/users",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.get("/users/{id}",
            tags=["Users"])
async def get_user(id: int,
                   authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response1 = requests.get(
            f"{DB_SERVER_URL}/users/{id}",
            headers={"Authorization": authorization}
        )
        user_details = response1.json()
        if len(user_details['data']) > 0:
            response2 = requests.get(
                f"{DB_SERVER_URL}/users/{id}/profiles",
                headers={"Authorization": authorization}
            )
            profiles = response2.json()
            user_details['data'][0]['profiles'] = get_user_profiles(profiles['data'])
        return JSONResponse(
            status_code=response1.status_code,
            content=user_details
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/users/{id}",
               tags=["Users"])
async def delete_user(id: int,
                      authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.delete(
            f"{DB_SERVER_URL}/users/{id}",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.put("/users/{id}",
            tags=["Users"])
async def put_user(id: int,
                   item: BaseUserIn,
                   authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.put(
            f"{DB_SERVER_URL}/users/{id}",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/users/{user_id}/profiles/{profile_id}",
               tags=["Users"])
async def delete_user_profile(user_id: int,
                              profile_id: int,
                              authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.delete(
            f"{DB_SERVER_URL}/users/{user_id}/profiles/{profile_id}",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.post("/users/profiles",
             tags=["Users"])
async def post_user_profile(item: UserProfileIn,
                            authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.post(
            f"{DB_SERVER_URL}/users/profiles",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)