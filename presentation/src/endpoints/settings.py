from fastapi import APIRouter, status, Request, Form
import requests
from fastapi.responses import RedirectResponse

from settings import BL_SERVER_URL, templates
from src.utils.base_utils import raise_exception
from src.utils.authorization_utils import AuthorizationUser

router = APIRouter()


@router.get("/settings",
            tags=["Settings"])
async def get_settings(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        devices_details = requests.get(f"{BL_SERVER_URL}/devices", headers={"Authorization": authorization})
        if devices_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'settings.html',
            context={
                'request': request,
                'data_list': (devices_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.put("/settings/{id}",
            tags=["Settings"])
async def put_settings(request: Request,
                       id: int,
                       description: str = Form(...),
                       limit: float = Form(...)
                       ):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        put_resp = requests.put(f"{BL_SERVER_URL}/devices/{id}",
                                headers={"Authorization": authorization},
                                json={
                                    'description': description,
                                    'limit': limit
                                })
        devices_details = requests.get(f"{BL_SERVER_URL}/devices", headers={"Authorization": authorization})
        if devices_details.status_code == status.HTTP_401_UNAUTHORIZED or \
                put_resp.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'settings.html',
            context={
                'request': request,
                'data_list': (devices_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)
