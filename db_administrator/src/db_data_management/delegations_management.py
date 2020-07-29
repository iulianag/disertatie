from sqlalchemy import select
from sqlalchemy import and_
from fastapi import status
from fastapi.encoders import jsonable_encoder

from settings import database
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.database_models.delegation import delegation
from src.database_models.profile import profile
from src.database_models.user import user


class DelegationsTableManager(object):
    @classmethod
    async def delete_delegation(cls, profile_id, user_id):
        query = delegation.select().where(and_(delegation.c.profile_id == profile_id,
                                               delegation.c.user_id == user_id))
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
        delete_query = delegation.delete().where(and_(delegation.c.profile_id == profile_id,
                                                      delegation.c.user_id == user_id))
        return not (bool(await database.execute(delete_query)))

    @classmethod
    async def read_delegations(cls, user_id=None, profile_id=None):
        join_condition = user\
            .join(delegation, delegation.c.user_id == user.c.id)\
            .join(profile, profile.c.id == delegation.c.profile_id)
        query = select([user.c.id.label('user_id'),
                        user.c.username.label('username'),
                        profile.c.id.label('profile_id'),
                        profile.c.name.label('profilename')])\
            .select_from(join_condition)
        if profile_id:
            query = query.where(profile.c.id == profile_id)
        if user_id:
            query = query.where(user.c.id == user_id)
        return await database.fetch_all(query)

    @classmethod
    async def create_delegation(cls, schema):
        query = delegation.insert().values(**schema.dict())
        await database.execute(query)
        return {
            **schema.dict()
        }
