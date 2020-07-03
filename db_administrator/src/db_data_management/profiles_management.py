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
        query = profile.select().where(profile.c.name == profilename)
        record = await database.fetch_one(query)
        if not record:
            return
        return record['id']
