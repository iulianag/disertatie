from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/device_groups", tags=["device_groups"])
async def get_device_groups():
    return {"device_groupname": "fakecurrentdevice_group"}


@router.post("/device_groups", tags=["device_groups"])
async def post_device_group():
    return {"device_groupname": "fakecurrentdevice_group"}


@router.delete("/device_groups", tags=["device_groups"])
async def delete_device_group():
    return {"device_groupname": "fakecurrentdevice_group"}
