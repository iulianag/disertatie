from fastapi import APIRouter, status, Security
from fastapi.security import APIKeyHeader
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests

from settings import DB_SERVER_URL
from src.utils.base_utils import raise_exception
from src.validation_models.user_model import UserCredentialsIn

router = APIRouter()


@router.post("/login",
             tags=["authorization"])
async def login(item: UserCredentialsIn):
    try:
        response = requests.post(f"{DB_SERVER_URL}/login", json=item.dict())
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)


@router.post("/logout",
             tags=["authorization"])
async def logout(authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    try:
        response = requests.post(f"{DB_SERVER_URL}/logout", headers={"Authorization": authorization})
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=response.json()
        )
    except Exception as e:
        raise_exception(e)
