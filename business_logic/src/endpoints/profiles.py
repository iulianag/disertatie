from fastapi import APIRouter, Query, Security
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
import requests

from settings import DB_SERVER_URL
from src.utils.base_utils import raise_exception
from src.validation_models.profile_model import ProfileIn, BaseProfileIn, ProfileGroupIn
from src.utils.profile_utils import get_profile_users, get_profile_groups


router = APIRouter()


@router.get("/profiles",
            tags=["profiles"])
async def get_profiles(query: str = Query(None),
                       authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.get(
            f"{DB_SERVER_URL}/profiles",
            headers={"Authorization": authorization},
            params={'query': query}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.post("/profiles",
             tags=["profiles"])
async def post_profile(item: ProfileIn,
                       authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.post(
            f"{DB_SERVER_URL}/profiles",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.get("/profiles/{id}",
            tags=["profiles"])
async def get_profile(id: int,
                      authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response1 = requests.get(
            f"{DB_SERVER_URL}/profiles/{id}",
            headers={"Authorization": authorization}
        )
        profile_details = response1.json()
        if len(profile_details['data']) > 0:
            response2 = requests.get(
                f"{DB_SERVER_URL}/profiles/{id}/users",
                headers={"Authorization": authorization}
            )
            users = response2.json()
            profile_details['data'][0]['users'] = get_profile_users(users['data'])

            response3 = requests.get(
                f"{DB_SERVER_URL}/profiles/{id}/groups",
                headers={"Authorization": authorization}
            )
            groups = response3.json()
            profile_details['data'][0]['groups'] = get_profile_groups(groups['data'])
        return JSONResponse(
            status_code=response1.status_code,
            content=profile_details
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/profiles/{id}",
               tags=["profiles"])
async def delete_profile(id: int,
                         authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.delete(
            f"{DB_SERVER_URL}/profiles/{id}",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.put("/profiles/{id}",
            tags=["profiles"])
async def put_profile(id: int,
                      item: BaseProfileIn,
                      authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.put(
            f"{DB_SERVER_URL}/profiles/{id}",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/profiles/{profile_id}/groups/{group_id}",
               tags=["profiles"])
async def delete_profile_group(profile_id: int,
                               group_id: int,
                               authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.delete(
            f"{DB_SERVER_URL}/profiles/{profile_id}/groups/{group_id}",
            headers={"Authorization": authorization}
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.post("/profiles/groups",
             tags=["profiles"])
async def post_profile_group(item: ProfileGroupIn,
                             authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.post(
            f"{DB_SERVER_URL}/profiles/groups",
            headers={"Authorization": authorization},
            json=item.dict()
        )
        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)
