from fastapi import APIRouter, status, Request, Form
import requests
from fastapi.responses import RedirectResponse

from settings import BL_SERVER_URL, templates
from src.utils.base_utils import raise_exception
from src.utils.authorization_utils import AuthorizationUser

router = APIRouter()


@router.get("/devices",
            tags=["Devices"])
async def get_devices(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        devices_details = requests.get(f"{BL_SERVER_URL}/devices", headers={"Authorization": authorization})
        if devices_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'devices.html',
            context={
                'request': request,
                'data_list': (devices_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.post("/devices",
             tags=["Devices"])
async def post_devices(request: Request,
                       name: str = Form(...),
                       description: str = Form(...),
                       limit: float = Form(...),
                       typeId: int = Form(...)):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        devices_details = requests.post(f"{BL_SERVER_URL}/devices",
                                        headers={"Authorization": authorization},
                                        json={
                                             'name': name,
                                             'description': description,
                                             'limit': limit,
                                             'type_id': typeId
                                        })
        if devices_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'device.html',
            context={
                'request': request,
                'data_list': (devices_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.get("/devices/{id}",
            tags=["Devices"])
async def get_device(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        device_details = requests.get(f"{BL_SERVER_URL}/devices/{id}", headers={"Authorization": authorization})
        if device_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'device.html',
            context={
                'request': request,
                'data_list': (device_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.delete("/devices/{id}",
               tags=["Devices"])
async def delete_device(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        delete_resp = requests.delete(f"{BL_SERVER_URL}/devices/{id}", headers={"Authorization": authorization})
        devices_details = requests.get(f"{BL_SERVER_URL}/devices", headers={"Authorization": authorization})
        if delete_resp.status_code == status.HTTP_401_UNAUTHORIZED or \
                devices_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'users.html',
            context={
                'request': request,
                'data_list': (devices_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)
