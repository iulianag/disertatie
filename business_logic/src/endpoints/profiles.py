from fastapi import APIRouter, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.utils.base_utils import raise_exception
from src.validation_models.profile_model import ProfileIn, BaseProfileIn
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


router = APIRouter()


@router.get("/profiles",
            tags=["profiles"])
async def get_profiles(query: str = Query(None)):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.post("/profiles",
             tags=["profiles"])
async def post_profile(item: ProfileIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.get("/profiles/{profile_id}",
            tags=["profiles"])
async def get_profile(profile_id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.delete("/profiles/{profile_id}",
               tags=["profiles"])
async def delete_profile(id: int):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.put("/profiles/{profile_id}",
            tags=["profiles"])
async def put_profile(id: int, item: BaseProfileIn):
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)
