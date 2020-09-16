from fastapi import status
from fastapi.encoders import jsonable_encoder

from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from settings import templates


def raise_exception(e, request):
    if isinstance(e, CustomHTTPException):
        status_code = e.status_code
        message = e.content.get('info')
    else:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        message = 'Internal server error'
    return templates.TemplateResponse(
        'error_page.html',
        context={
            'request': request,
            'error_message': message,
            'status_code': status_code
        },
        status_code=status_code
    )
