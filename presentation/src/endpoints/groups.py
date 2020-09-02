from fastapi import APIRouter, status, Request, Form
import requests
from fastapi.responses import RedirectResponse

from settings import BL_SERVER_URL, templates
from src.utils.base_utils import raise_exception
from src.utils.authorization_utils import AuthorizationUser

router = APIRouter()


@router.get("/groups",
            tags=["Groups"])
async def get_groups(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        groups_details = requests.get(f"{BL_SERVER_URL}/groups", headers={"Authorization": authorization})
        if groups_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'groups.html',
            context={
                'request': request,
                'data_list': (groups_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.post("/groups",
             tags=["Groups"])
async def post_groups(request: Request,
                      name: str = Form(...),
                      description: str = Form(...)):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        groups_details = requests.post(f"{BL_SERVER_URL}/groups",
                                       headers={"Authorization": authorization},
                                       json={
                                             'name': name,
                                             'description': description
                                       })
        if groups_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'group.html',
            context={
                'request': request,
                'data_list': (groups_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.get("/groups/{id}",
            tags=["Groups"])
async def get_group(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        group_details = requests.get(f"{BL_SERVER_URL}/groups/{id}", headers={"Authorization": authorization})
        if group_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'group.html',
            context={
                'request': request,
                'data_list': (group_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)