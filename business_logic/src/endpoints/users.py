from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.validation_models.user_model import UserIn, BaseUserIn
from src.utils.base_utils import raise_exception
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel

router = APIRouter()


@router.get("/users",
            tags=["Users"])
async def get_users(query: str = Query(None)):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.post("/users",
             tags=["Users"])
async def post_user(item: UserIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.get("/users/{id}",
            tags=["Users"])
async def get_user(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.delete("/users/{id}",
               tags=["Users"])
async def delete_user(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.put("/users/{id}",
            tags=["Users"])
async def put_user(id: int, item: BaseUserIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)
