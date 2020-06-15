from sqlalchemy import select
from sqlalchemy import and_
import datetime
from fastapi import status
from fastapi.encoders import jsonable_encoder

from settings import database
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.db_data_management.base_management import BaseManager
from src.database_models.responsibility import responsibility
from src.database_models.profile import profile
from src.database_models.group import group


class ResponsibilitiesTableManager(BaseManager):
    @classmethod
    async def delete_responsibility(cls, profile_id, group_id):
        query = responsibility.select().where(and_(responsibility.c.profile_id == profile_id,
                                                   responsibility.c.group_id == group_id))
        record = await database.execute(query)
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
        delete_query = responsibility.delete().where(and_(responsibility.c.profile_id == profile_id,
                                                          responsibility.c.group_id == group_id))
        return not (bool(await database.execute(delete_query)))

    @classmethod
    async def read_responsibilities(cls, profile_id=None, group_id=None):
        join_condition = profile\
            .join(responsibility, responsibility.c.device_id == profile.c.id)\
            .join(group, group.c.id == responsibility.c.group_id)
        query = select([profile.c.id.label('profile_id'),
                        profile.c.profilename.label('profilename'),
                        group.c.id.label('group_id'),
                        group.c.groupname.label('groupname')])\
            .select_from(join_condition)
        if profile_id:
            query = query.where(profile.c.id == profile_id)
        if group_id:
            query = query.where(group.c.id == group_id)
        return await database.fetch_all(query)
