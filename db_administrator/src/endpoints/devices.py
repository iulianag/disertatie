from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.user_permission import have_permission
from src.dependencies.user_permission import is_admin
from src.dependencies.authorization import is_authenticated
from src.utils.base_utils import raise_exception
from src.db_data_management.devices_management import DevicesTableManager

from src.db_data_management.users_management import UsersTableManager
from src.database_models.device import device
from src.utils.device_utils import get_device_list, get_device_details
from src.utils.user_utils import get_user_device_id_list
from src.validation_models.device_model import DeviceIn, BaseDeviceIn
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


router = APIRouter()


@router.get("/devices",
            tags=["devices"])
async def get_devices(query: str = Query(None),
                      type_name: str = Query(None),
                      user_details: dict = Depends(is_authenticated)):
    try:
        user_device_id_list = get_user_device_id_list(
            await UsersTableManager.get_user_devices(
                user_details['id'],
                await is_admin(user_details['id'])
            )
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_list(
                    await DevicesTableManager.read_all_records(
                        table=device,
                        filter_query=query,
                        type_name=type_name,
                        device_id_list=user_device_id_list
                    )
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/devices",
             tags=["devices"])
async def post_device(item: DeviceIn,
                      user_details: dict = Depends(is_authenticated)):
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
            tags=["devices"])
async def get_device(id: int,
                     user_details: dict = Depends(is_authenticated)):
    try:
        user_device_id_list = get_user_device_id_list(
            await UsersTableManager.get_user_devices(
                user_details['id'],
                await is_admin(user_details['id'])
            )
        )
        if id in user_device_id_list:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(
                    get_device_details(await DevicesTableManager.read_record(device, id))
                )
            )
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='error', message='Permission denied'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/devices/{id}",
               tags=["devices"])
async def delete_device(id: int,
                        user_details: dict = Depends(is_authenticated)):
    try:
        user_device_id_list = get_user_device_id_list(
            await UsersTableManager.get_user_devices(
                user_details['id'],
                await is_admin(user_details['id'])
            )
        )
        if id in user_device_id_list:
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
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='error', message='Permission denied'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.put("/devices/{id}",
            tags=["devices"])
async def put_device(id: int,
                     item: BaseDeviceIn,
                     user_details: dict = Depends(is_authenticated)):
    try:
        user_device_id_list = get_user_device_id_list(
            await UsersTableManager.get_user_devices(
                user_details['id'],
                await is_admin(user_details['id'])
            )
        )
        if id in user_device_id_list:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(
                    get_device_details(await DevicesTableManager.update_record(device, id, item))
                )
            )
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='error', message='Permission denied'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)
