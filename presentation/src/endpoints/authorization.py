from fastapi import APIRouter, status, Security, Request, Form, Depends
from fastapi.security.api_key import APIKeyHeader, APIKeyCookie, APIKey
from fastapi.responses import JSONResponse
import requests
from fastapi.responses import RedirectResponse

from settings import BL_SERVER_URL, templates
from src.utils.base_utils import raise_exception
from src.utils.authorization_utils import AuthorizationUser
from src.dependencies.authorization import is_authenticated

router = APIRouter()


@router.get("/",
            tags=["authorization"])
async def index(request: Request):
    try:
        authorization = AuthorizationUser.active_user_token.get(request.client.host, None)
        if not authorization:
            return templates.TemplateResponse(
                'login.html',
                context={'request': request},
                status_code=status.HTTP_200_OK
            )
        response = RedirectResponse('/home')
        return response
    except Exception as e:
        raise_exception(e)


@router.post("/",
             tags=["authorization"])
async def login(request: Request,
                username: str = Form(...),
                password: str = Form(...)):
    try:
        response = requests.post(f"{BL_SERVER_URL}/login",
                                 json={"username": username, "password": password})
        if response.status_code == status.HTTP_200_OK:
            response_json = response.json()
            authorization = response_json['data'][0]['token']
            user_profile = requests.get(f"{BL_SERVER_URL}/", headers={"Authorization": authorization})
            AuthorizationUser.set_online_user(request.client.host, username, authorization)
            response = templates.TemplateResponse(
                'home.html',
                context={'request': request, 'data_list': user_profile.json()},
                status_code=status.HTTP_200_OK
            )
            return response
        else:
            return templates.TemplateResponse(
                'login.html',
                context={'request': request},
                status_code=response.status_code
            )
    except Exception as e:
        raise_exception(e)


@router.get("/home",
            tags=["authorization"])
async def home(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        user_details = requests.get(f"{BL_SERVER_URL}/", headers={"Authorization": authorization})
        if user_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'home.html',
            context={'request': request, 'data_list': user_details.json()},
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.get("/logout",
            tags=["authorization"])
async def logout(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if authorization:
            logout_response = requests.post(f"{BL_SERVER_URL}/logout", headers={"Authorization": authorization})
        AuthorizationUser.logout_user(request.client.host)
        return RedirectResponse(url='/home')
    except Exception as e:
        raise_exception(e)

