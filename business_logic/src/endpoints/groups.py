from fastapi import APIRouter, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.utils.base_utils import raise_exception
from src.validation_models.group_model import BaseGroupIn, GroupIn
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel

router = APIRouter()


@router.get("/groups",
            tags=["groups"])
async def get_groups(query: str = Query(None)):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.post("/groups",
             tags=["groups"])
async def post_group(item: GroupIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.get("/groups/{group_id}",
            tags=["groups"])
async def get_group(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.delete("/groups/{group_id}",
               tags=["groups"])
async def delete_group(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.put("/groups/{group_id}",
            tags=["groups"])
async def put_group(id: int, item: BaseGroupIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)