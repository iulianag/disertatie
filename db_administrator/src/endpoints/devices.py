from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.user_permission import have_permission
from src.utils.base_utils import raise_exception
from src.db_data_management.devices_management import DevicesTableManager
from src.database_models.device import device
from src.utils.device_utils import get_device_list, get_device_details
from src.validation_models.device_model import DeviceIn, BaseDeviceIn
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


router = APIRouter()


@router.get("/devices",
            tags=["devices"],
            dependencies=[Depends(have_permission)])
async def get_devices(query: str = Query(None), type_name: str = Query(None)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_list(await DevicesTableManager.read_all_records(device, query, type_name))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/devices",
             tags=["devices"],
             dependencies=[Depends(have_permission)])
async def post_device(item: DeviceIn):
    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                get_device_details(await DevicesTableManager.create_record(device, item))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/devices/{id}",
            tags=["devices"],
            dependencies=[Depends(have_permission)])
async def get_device(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_details(await DevicesTableManager.read_record(device, id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/devices/{id}",
               tags=["devices"],
               dependencies=[Depends(have_permission)])
async def delete_device(id: int):
    try:
        await DevicesTableManager.delete_record(device, id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Device deleted successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.put("/devices/{id}",
            tags=["devices"],
            dependencies=[Depends(have_permission)])
async def put_device(id: int, item: BaseDeviceIn):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_details(await DevicesTableManager.update_record(device, id, item))
            )
        )
    except Exception as e:
        raise_exception(e)
