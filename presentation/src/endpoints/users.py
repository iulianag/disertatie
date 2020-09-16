from fastapi import APIRouter, status, Request, Form
import requests
from fastapi.responses import RedirectResponse

from settings import BL_SERVER_URL, templates, pwd_context
from src.utils.base_utils import raise_exception
from src.utils.authorization_utils import AuthorizationUser

router = APIRouter()


@router.get("/users",
            tags=["Users"])
async def get_users(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        users_details = requests.get(f"{BL_SERVER_URL}/users", headers={"Authorization": authorization})
        if users_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'users.html',
            context={
                'request': request,
                'data_list': (users_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        return raise_exception(e, request)


@router.post("/users",
             tags=["Users"])
async def post_users(request: Request,
                     username: str = Form(...),
                     password: str = Form(...),
                     fullName: str = Form(...),
                     email: str = Form(...)):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        users_details = requests.post(f"{BL_SERVER_URL}/users",
                                      headers={"Authorization": authorization},
                                      json={
                                          'username': username,
                                          'password': pwd_context.encrypt(password),
                                          'full_name': fullName,
                                          'email': email
                                      })
        if users_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'user.html',
            context={
                'request': request,
                'data_list': (users_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        return raise_exception(e, request)


@router.get("/users/{id}",
            tags=["Users"])
async def get_user(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        user_details = requests.get(f"{BL_SERVER_URL}/users/{id}", headers={"Authorization": authorization})
        if user_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'user.html',
            context={
                'request': request,
                'data_list': (user_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        return raise_exception(e, request)


@router.delete("/users/{id}",
               tags=["Users"])
async def delete_user(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        delete_user_resp = requests.delete(f"{BL_SERVER_URL}/users/{id}", headers={"Authorization": authorization})
        users_details = requests.get(f"{BL_SERVER_URL}/users", headers={"Authorization": authorization})
        if delete_user_resp.status_code == status.HTTP_401_UNAUTHORIZED or \
                users_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'users.html',
            context={
                'request': request,
                'data_list': (users_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        return raise_exception(e, request)


@router.put("/users/{id}",
            tags=["Users"])
async def put_users(request: Request,
                    id: int,
                    fullName: str = Form(...),
                    email: str = Form(...)):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        put_resp = requests.put(f"{BL_SERVER_URL}/users/{id}",
                                headers={"Authorization": authorization},
                                json={
                                    'full_name': fullName,
                                    'email': email
                                })
        users_details = requests.get(f"{BL_SERVER_URL}/users", headers={"Authorization": authorization})
        if users_details.status_code == status.HTTP_401_UNAUTHORIZED or \
                put_resp.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'users.html',
            context={
                'request': request,
                'data_list': (users_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        return raise_exception(e, request)


@router.post("/users/profiles",
             tags=["Users"])
async def post_user_profile(request: Request,
                            userId: int = Form(...),
                            profileId: int = Form(...)):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        users_details = requests.post(f"{BL_SERVER_URL}/users/profiles",
                                      headers={"Authorization": authorization},
                                      json={
                                          'user_id': userId,
                                          'profile_id': profileId
                                      })
        if users_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        user_details = requests.get(f"{BL_SERVER_URL}/users/{userId}", headers={"Authorization": authorization})
        response = templates.TemplateResponse(
            'user.html',
            context={
                'request': request,
                'data_list': (user_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        return raise_exception(e, request)


@router.delete("/users/{userId}/profiles/{profileId}",
               tags=["Users"])
async def delete_user_profile(request: Request,
                              userId: int,
                              profileId: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        delete_user_resp = requests.delete(
            f"{BL_SERVER_URL}/users/{userId}/profiles/{profileId}",
            headers={"Authorization": authorization}
        )
        if delete_user_resp.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        user_details = requests.get(f"{BL_SERVER_URL}/users/{userId}", headers={"Authorization": authorization})
        response = templates.TemplateResponse(
            'user.html',
            context={
                'request': request,
                'data_list': (user_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        return raise_exception(e, request)