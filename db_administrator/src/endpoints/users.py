from fastapi import APIRouter, Depends, status, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies.authorization import is_authenticated
from src.db_data_management.users_management import UsersTableManager
from src.utils.user_utils import get_user_details, get_users_list
from src.database_models.user import user
from src.validation_models.user_model import UserIn, BaseUserIn
from src.utils.base_utils import raise_exception
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel

router = APIRouter()


@router.get("/users",
            tags=["Users"])
async def get_users(query: str = Query(None), user_id=Depends(is_authenticated)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_users_list(await UsersTableManager.read_all_records(user, query))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.post("/users", tags=["Users"])
async def post_user(item: UserIn, user_id=Depends(is_authenticated)):
    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder(
                get_user_details(await UsersTableManager.create_record(user, item))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.get("/users/{id}", tags=["Users"])
async def get_user(id: int, user_id=Depends(is_authenticated)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_user_details(await UsersTableManager.read_record(user, id))
            )
        )
    except Exception as e:
        raise_exception(e)


@router.delete("/users/{id}", tags=["Users"])
async def delete_user(id: int, user_id=Depends(is_authenticated)):
    try:
        await UsersTableManager.delete_record(user, id)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='User deleted successfully'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)


@router.put("/users/{id}", tags=["Users"])
async def put_user(id: int, item: BaseUserIn, user_id=Depends(is_authenticated)):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                get_user_details(await UsersTableManager.update_record(user, id, item))
            )
        )
    except Exception as e:
        raise_exception(e)
