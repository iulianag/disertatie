from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.user_permission import have_permission
from src.utils.base_utils import raise_exception
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.db_data_management.groups_management import GroupsTableManager
from src.database_models.group import group
from src.utils.group_utils import get_group_details, get_groups_list
from src.validation_models.group_model import BaseGroupIn, GroupIn

router = APIRouter()


@router.get("/groups",
            tags=["groups"],
            dependencies=[Depends(have_permission)])
async def get_groups(query: str = Query(None)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_groups_list(await GroupsTableManager.read_all_records(group, query))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/groups",
             tags=["groups"],
             dependencies=[Depends(have_permission)])
async def post_group(item: GroupIn):
    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                get_group_details(await GroupsTableManager.create_record(group, item))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/groups/{group_id}",
            tags=["groups"],
            dependencies=[Depends(have_permission)])
async def get_group(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_group_details(await GroupsTableManager.read_record(group, id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/groups/{group_id}",
               tags=["groups"],
               dependencies=[Depends(have_permission)])
async def delete_group(id: int):
    try:
        await GroupsTableManager.delete_record(group, id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Group deleted successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.put("/groups/{group_id}",
            tags=["groups"],
            dependencies=[Depends(have_permission)])
async def put_group(id: int, item: BaseGroupIn):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_group_details(await GroupsTableManager.update_record(group, id, item))
            )
        )
    except Exception as e:
        raise_exception(e)