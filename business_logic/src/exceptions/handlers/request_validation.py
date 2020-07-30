from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from settings import app
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException


@app.exception_handler(CustomHTTPException)
async def unicorn_exception_handler(request: Request, exc: CustomHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.content,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    content = {
        'meta': {},
        'info': [],
        'data': []
    }
    for error in exc.errors():
        content['info'].append({
            'type': 'error',
            'message': f'Invalid {"->".join([str(item) for item in error["loc"][2:]])} format'
        })
    return JSONResponse(
        status_code=400,
        content=content,
    )