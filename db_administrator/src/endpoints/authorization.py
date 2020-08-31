import secrets

from fastapi import APIRouter, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.db_data_management.users_management import UsersTableManager
from src.validation_models.user_model import UserCredentialsIn, UserIn
from src.utils.base_utils import raise_exception
from src.validation_models.base_validation_model import BaseResponseModel, InfoModel
from src.dependencies.user_permission import is_authenticated
from src.database_models.user import user

router = APIRouter()


@router.post("/login",
             tags=["authorization"])
async def login(data: UserCredentialsIn):
    try:
        await UsersTableManager.validate_user_credentials(data.username, data.password)
        access_token = secrets.token_urlsafe(20)
        await UsersTableManager.update_token(data.username, access_token)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    data=[{"token": access_token}]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/",
            tags=["authorization"])
async def get_my_profile(user_details: dict = Depends(is_authenticated)):
    try:
        await UsersTableManager.update_token(user_details['username'])
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    data=[user_details]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/logout",
             tags=["authorization"])
async def logout(user_details: dict = Depends(is_authenticated)):
    try:
        await UsersTableManager.update_token(user_details['username'])
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='User logged out successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)
