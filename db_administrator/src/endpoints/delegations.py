from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.user_permission import have_permission
from src.utils.base_utils import raise_exception
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.db_data_management.delegations_management import DelegationsTableManager
from src.utils.delegation_utils import get_delegations_list, get_delegation_details
from src.validation_models.delegation_model import DelegationIn

router = APIRouter()


@router.get("/users/{id}/profiles",
            tags=["delegations"],
            dependencies=[Depends(have_permission)])
async def get_user_profiles(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_delegations_list(await DelegationsTableManager.read_delegations(user_id=id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/profiles/{id}/users",
            tags=["delegations"],
            dependencies=[Depends(have_permission)])
async def get_profile_users(id: int):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_delegations_list(await DelegationsTableManager.read_delegations(profile_id=id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/users/profiles", tags=["delegations"])
async def post_users_profiles(item: DelegationIn):
    try:
        await DelegationsTableManager.create_delegation(item)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Delegation added successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/users/{user_id}/profiles/{profile_id}",
               tags=["delegations"],
               dependencies=[Depends(have_permission)])
async def delete_delegation(user_id: int, profile_id: int):
    try:
        await DelegationsTableManager.delete_delegation(
            profile_id=profile_id,
            user_id=user_id
        )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Delegation deleted successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)
