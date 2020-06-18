

from fastapi import Security, status
from fastapi.security import APIKeyHeader
from fastapi.encoders import jsonable_encoder
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.db_data_management.profiles_management import ProfilesTableManager
from src.db_data_management.delegations_management import DelegationsTableManager
from src.dependencies.authorization import is_authenticated
from src.utils.delegation_utils import get_user_profile_id_list


async def have_permission(authorization=Security(APIKeyHeader(name="Authorization", auto_error=False))):
    user_id = await is_authenticated(authorization)
    profile_id = await ProfilesTableManager.get_profile_id_by_profilename('admin')
    user_profiles = get_user_profile_id_list(
        await DelegationsTableManager.read_delegations(user_id=user_id)
    )
    if profile_id not in user_profiles:
        raise CustomHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='error', message='You are not allowed to perform this action'
                    )]
                )
            )
        )
    return user_id


