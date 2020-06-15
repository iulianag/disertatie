from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.post("/login", tags=["authorization"])
async def login():
    return {"device_groupname": "fakecurrentdevice_group"}


@router.post("/logout", tags=["authorization"])
async def logout():
    return {"device_groupname": "fakecurrentdevice_group"}
