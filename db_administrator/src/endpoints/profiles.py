from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.user_permission import have_permission
from src.utils.base_utils import raise_exception
from src.database_models.profile import profile
from src.db_data_management.profiles_management import ProfilesTableManager
from src.utils.profile_utils import get_profiles_list, get_profile_details
from src.validation_models.profile_model import ProfileIn, BaseProfileIn
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


router = APIRouter()


@router.get("/profiles",
            tags=["profiles"],
            dependencies=[Depends(have_permission)])
async def get_profiles(query: str = Query(None)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_profiles_list(await ProfilesTableManager.read_all_records(profile, query))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/profiles",
             tags=["profiles"],
             dependencies=[Depends(have_permission)])
async def post_profile(item: ProfileIn):
    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                get_profile_details(await ProfilesTableManager.create_record(profile, item))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/profiles/{id}",
            tags=["profiles"],
            dependencies=[Depends(have_permission)])
async def get_profile(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_profile_details(await ProfilesTableManager.read_record(profile, id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/profiles/{id}",
               tags=["profiles"],
               dependencies=[Depends(have_permission)])
async def delete_profile(id: int):
    try:
        await ProfilesTableManager.delete_record(profile, id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Profile deleted successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.put("/profiles/{id}",
            tags=["profiles"],
            dependencies=[Depends(have_permission)])
async def put_profile(id: int, item: BaseProfileIn):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_profile_details(await ProfilesTableManager.update_record(profile, id, item))
            )
        )
    except Exception as e:
        raise_exception(e)
