from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.utils.base_utils import raise_exception

router = APIRouter()


@router.post("/login",
             tags=["authorization"])
async def login():
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)


@router.post("/logout",
             tags=["authorization"])
async def logout():
    try:
        return {"test": "fake result"}
    except Exception as e:
        raise_exception(e)
