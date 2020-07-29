from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.user_permission import have_permission
from src.utils.base_utils import raise_exception
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.db_data_management.device_group_manasgement import DevicegroupTableManager
from src.utils.device_group_utils import get_device_group_list
from src.validation_models.device_group_model import DevicegroupIn

router = APIRouter()


@router.get("/devices/{id}/groups",
            tags=["device_group"],
            dependencies=[Depends(have_permission)])
async def get_device_groups(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_group_list(await DevicegroupTableManager.read_devices_groups(device_id=id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/groups/{id}/devices",
            tags=["device_group"],
            dependencies=[Depends(have_permission)])
async def get_group_devices(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_group_list(await DevicegroupTableManager.read_devices_groups(group_id=id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/devices/groups",
             tags=["device_group"],
             dependencies=[Depends(have_permission)])
async def post_device_group(item: DevicegroupIn):
    try:
        await DevicegroupTableManager.create_device_group(item)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Devicegroup added successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/devices/{device_id}/groups/{group_id}",
               tags=["device_group"],
               dependencies=[Depends(have_permission)])
async def delete_device_group(device_id: int, group_id: int):
    try:
        await DevicegroupTableManager.delete_device_group(
            device_id=device_id,
            group_id=group_id
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Devicegroup deleted successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)
