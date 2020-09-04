from fastapi import APIRouter, status, Request, Form
import requests
from fastapi.responses import RedirectResponse

from settings import BL_SERVER_URL, templates
from src.utils.base_utils import raise_exception
from src.utils.authorization_utils import AuthorizationUser

router = APIRouter()


@router.get("/profiles",
            tags=["Profiles"])
async def get_profiles(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        profiles_details = requests.get(f"{BL_SERVER_URL}/profiles", headers={"Authorization": authorization})
        if profiles_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'profiles.html',
            context={
                'request': request,
                'data_list': (profiles_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.post("/profiles",
             tags=["Profiles"])
async def post_profiles(request: Request,
                        name: str = Form(...),
                        description: str = Form(...)):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        profiles_details = requests.post(f"{BL_SERVER_URL}/profiles",
                                         headers={"Authorization": authorization},
                                         json={
                                             'name': name,
                                             'description': description
                                         })
        if profiles_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'profile.html',
            context={
                'request': request,
                'data_list': (profiles_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.get("/profiles/{id}",
            tags=["Profiles"])
async def get_profile(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        profile_details = requests.get(f"{BL_SERVER_URL}/profiles/{id}", headers={"Authorization": authorization})
        if profile_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'profile.html',
            context={
                'request': request,
                'data_list': (profile_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.delete("/profiles/{id}",
               tags=["Profiles"])
async def delete_profile(request: Request, id: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        delete_resp = requests.delete(f"{BL_SERVER_URL}/profiles/{id}", headers={"Authorization": authorization})
        profiles_details = requests.get(f"{BL_SERVER_URL}/profiles", headers={"Authorization": authorization})
        if delete_resp.status_code == status.HTTP_401_UNAUTHORIZED or \
                profiles_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'profiles.html',
            context={
                'request': request,
                'data_list': (profiles_details.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.post("/profiles/groups",
             tags=["Profiles"])
async def post_profiles(request: Request,
                        profileId: int = Form(...),
                        groupId: int = Form(...)):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        profiles_details = requests.post(f"{BL_SERVER_URL}/profiles/groups",
                                         headers={"Authorization": authorization},
                                         json={
                                             'profile_id': profileId,
                                             'group_id': groupId
                                         })
        if profiles_details.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        profile_details = requests.get(
            f"{BL_SERVER_URL}/profiles/{profileId}", headers={"Authorization": authorization}
        )
        response = templates.TemplateResponse(
            'profile.html',
            context={
                'request': request,
                'data_list': (profile_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)


@router.delete("/profiles/{profileId}/groups/{groupId}",
               tags=["Profiles"])
async def delete_profile_group(request: Request,
                              profileId: int,
                              groupId: int):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        delete_resp = requests.delete(
            f"{BL_SERVER_URL}/profiles/{profileId}/groups/{groupId}",
            headers={"Authorization": authorization}
        )
        if delete_resp.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        profile_details = requests.get(f"{BL_SERVER_URL}/profiles/{profileId}", headers={"Authorization": authorization})
        response = templates.TemplateResponse(
            'profile.html',
            context={
                'request': request,
                'data_list': (profile_details.json())['data'][0]
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)
