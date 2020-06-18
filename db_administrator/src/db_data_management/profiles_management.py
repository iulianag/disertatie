from fastapi import status
from fastapi.encoders import jsonable_encoder

from settings import database
from src.db_data_management.base_management import BaseManager
from src.database_models.profile import profile
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


class ProfilesTableManager(BaseManager):
    @classmethod
    async def get_profile_id_by_profilename(cls, profilename):
        query = profile.select().where(profile.c.profilename == profilename)
        record = await database.fetch_one(query)
        if not record:
            raise CustomHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                content=jsonable_encoder(
                    BaseResponseModel(
                        info=[InfoModel(
                            type='error', message='Item not found'
                        )]
                    )
                )
            )
        return record['id']
