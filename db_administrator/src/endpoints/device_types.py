from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.user_permission import have_permission
from src.db_data_management.devices_types_management import DevicesTypesTableManager
from src.utils.device_type_utils import get_device_type_details, get_device_type_list
from src.database_models.device_type import device_type
from src.validation_models.device_type_model import DeviceTypeIn, BaseDeviceTypeIn
from src.utils.base_utils import raise_exception
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


router = APIRouter()


@router.get("/types",
            tags=["types"],
            dependencies=[Depends(have_permission)])
async def get_types(query: str = Query(None)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_type_list(await DevicesTypesTableManager.read_all_records(device_type, query))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/types",
             tags=["types"],
             dependencies=[Depends(have_permission)])
async def post_type(item: DeviceTypeIn):
    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                get_device_type_details(await DevicesTypesTableManager.create_record(device_type, item))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/types/{type_id}",
            tags=["types"],
            dependencies=[Depends(have_permission)])
async def get_type(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_type_details(await DevicesTypesTableManager.read_record(device_type, id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/types/{type_id}",
               tags=["types"],
               dependencies=[Depends(have_permission)])
async def delete_type(id: int):
    try:
        await DevicesTypesTableManager.delete_record(device_type, id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Device type deleted successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.put("/types/{type_id}",
            tags=["types"],
            dependencies=[Depends(have_permission)])
async def put_type(id: int, item: BaseDeviceTypeIn):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_device_type_details(await DevicesTypesTableManager.update_record(device_type, id, item))
            )
        )
    except Exception as e:
        raise_exception(e)