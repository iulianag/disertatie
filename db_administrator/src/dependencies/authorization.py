from fastapi import Security, status
from fastapi.security import APIKeyHeader
from fastapi.encoders import jsonable_encoder
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.db_data_management.users_management import UsersTableManager


async def is_authenticated(authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    if not authorization:
        raise CustomHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='error', message='Unauthorized'
                    )]
                )
            )
        )
    user_id = await UsersTableManager.is_valid_token(authorization)
    if not user_id:
        raise CustomHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='error', message='You are not authenticated'
                    )]
                )
            )
        )
    return user_id
