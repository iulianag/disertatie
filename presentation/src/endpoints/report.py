from fastapi import APIRouter, status, Request
from fastapi.responses import RedirectResponse
import requests

from settings import BL_SERVER_URL, templates
from src.utils.base_utils import raise_exception
from src.utils.authorization_utils import AuthorizationUser

router = APIRouter()


@router.get("/realTimeValues",
            tags=["Reports"])
async def real_time_values(request: Request):
    try:
        authorization = AuthorizationUser.get_token(request.client.host)
        if not authorization:
            return RedirectResponse('/')
        sensors_values = requests.get(f"{BL_SERVER_URL}/realTimeValues", headers={"Authorization": authorization})
        if sensors_values.status_code == status.HTTP_401_UNAUTHORIZED:
            AuthorizationUser.logout_user(request.client.host)
            return RedirectResponse('/')
        response = templates.TemplateResponse(
            'real_time_values.html',
            context={
                'request': request,
                'data_list': (sensors_values.json())['data']
            },
            status_code=status.HTTP_200_OK
        )
        return response
    except Exception as e:
        raise_exception(e)
