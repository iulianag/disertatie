from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()


@router.get("/devices", tags=["devices"])
async def get_devices():
    return {"devicename": "fakecurrentdevice"}


@router.post("/devices", tags=["devices"])
async def post_device():
    return {"devicename": "fakecurrentdevice"}


@router.get("/devices/{device_id}", tags=["devices"])
async def get_device(device_id: int):
    return {"devicename": "fakecurrentdevice"}


@router.delete("/devices/{device_id}", tags=["devices"])
async def delete_device(device_id: int):
    return {"devicename": "fakecurrentdevice"}


@router.put("/devices/{device_id}", tags=["devices"])
async def put_device(device_id: int):
    return {"devicename": "fakecurrentdevice"}