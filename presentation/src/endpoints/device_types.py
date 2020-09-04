from fastapi import APIRouter, status, Request, Form
import requests
from fastapi.responses import RedirectResponse

from settings import BL_SERVER_URL, templates
from src.utils.base_utils import raise_exception
from src.utils.authorization_utils import AuthorizationUser

router = APIRouter()


@router.get("/types",
            tags=["Types"])
async def get_types(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        types_details = requests.get(f"{BL_SERVER_URL}/types", headers={"Authorization": authorization})
        if types_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'device_types.html',
            context={
                'request': request,
                'data_list': (types_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.post("/types",
             tags=["Types"])
async def post_types(request: Request,
                     name: str = Form(...),
                     description: str = Form(...),
                     unit: str = Form(...)):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        typess_details = requests.post(f"{BL_SERVER_URL}/types",
                                       headers={"Authorization": authorization},
                                       json={
                                             'name': name,
                                             'description': description,
                                             'unit': unit
                                       })
        if typess_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'device_type.html',
            context={
                'request': request,
                'data_list': (typess_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.get("/types/{id}",
            tags=["Types"])
async def get_type(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        types_details = requests.get(f"{BL_SERVER_URL}/types/{id}", headers={"Authorization": authorization})
        if types_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'device_type.html',
            context={
                'request': request,
                'data_list': (types_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.delete("/types/{id}",
               tags=["Types"])
async def delete_type(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        delete_resp = requests.delete(f"{BL_SERVER_URL}/types/{id}", headers={"Authorization": authorization})
        type_details = requests.get(f"{BL_SERVER_URL}/types", headers={"Authorization": authorization})
        if delete_resp.status_code == status.HTTP_401_UNAUTHORIZED or \
                type_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'users.html',
            context={
                'request': request,
                'data_list': (type_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)
