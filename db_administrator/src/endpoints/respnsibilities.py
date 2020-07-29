from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.user_permission import have_permission
from src.utils.base_utils import raise_exception
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.db_data_management.responsibilities_management import ResponsibilitiesTableManager
from src.validation_models.responsibility_model import ResponsibilityIn
from src.utils.responsibility_utils import get_profile_group_list


router = APIRouter()


@router.get("/profiles/{id}/groups",
            tags=["responsibilities"],
            dependencies=[Depends(have_permission)])
async def get_profile_groups(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_profile_group_list(await ResponsibilitiesTableManager.read_responsibilities(profile_id=id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/groups/{id}/profiles",
            tags=["responsibilities"],
            dependencies=[Depends(have_permission)])
async def get_group_profiles(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_profile_group_list(await ResponsibilitiesTableManager.read_responsibilities(group_id=id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/profiles/groups",
             tags=["responsibilities"],
             dependencies=[Depends(have_permission)])
async def post_responsibility(item: ResponsibilityIn):
    try:
        await ResponsibilitiesTableManager.create_responsibility(item)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Responsibility added successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/profiles/{profile_id}/groups/{group_id}",
               tags=["responsibilities"],
               dependencies=[Depends(have_permission)])
async def delete_responsibility(profile_id: int, group_id: int):
    try:
        await ResponsibilitiesTableManager.delete_responsibility(
            profile_id=profile_id,
            group_id=group_id
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Responsibility deleted successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)
