from fastapi import status
from fastapi.encoders import jsonable_encoder

from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


def raise_exception(e):
    if isinstance(e, CustomHTTPException):
        raise e
    raise CustomHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='error', message='Internal server error: ' + e.args[0]
                    )]
                )
            )
        )