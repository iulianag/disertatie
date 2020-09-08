from sqlalchemy import and_, or_
from sqlalchemy import select
import datetime
from fastapi import status
from fastapi.encoders import jsonable_encoder

from settings import database, pwd_context
from src.db_data_management.base_management import BaseManager
from src.database_models.user import user
from src.database_models.delegation import delegation
from src.database_models.responsibility import responsibility
from src.database_models.device_group import device_group
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


class UsersTableManager(BaseManager):
    @classmethod
    async def extend_session(cls, username):
        extend_session_query = user.update()\
            .where(user.c.username == username)\
            .values({user.c.login_date: datetime.datetime.utcnow()})
        await database.execute(extend_session_query)

    @classmethod
    async def update_token(cls, username, token=None):
        update_query = user.update()\
            .where(user.c.username == username)\
            .values({user.c.session_token: token,
                     user.c.login_date: datetime.datetime.utcnow()})
        await database.execute(update_query)

    @classmethod
    async def is_valid_token(cls, token):
        login_date_limit = datetime.datetime.utcnow() - datetime.timedelta(minutes=60)
        query = user.select().where(and_(user.c.session_token == token,
                                         user.c.login_date > login_date_limit))
        user_details = await database.fetch_one(query)
        if not user_details:
            return False
        await cls.extend_session(user_details['username'])
        return user_details

    @classmethod
    async def read_all_records(cls, table, filter_query=None):
        query = table.select()
        if filter_query:
            query = query.where(or_(table.c.username.ilike(f'%{filter_query}%'),
                                    table.c.full_name.ilike(f'%{filter_query}%'),
                                    table.c.email.ilike(f'%{filter_query}%')
                                    )
                                )
        return await database.fetch_all(query)

    @classmethod
    async def validate_user_credentials(cls, username, password):
        query = user.select().where(user.c.username == username)
        record = await database.fetch_one(query)
        if not record:
            raise CustomHTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                content=jsonable_encoder(
                    BaseResponseModel(
                        info=[InfoModel(
                            type='error', message='User not found'
                        )]
                    )
                )
            )
        if not pwd_context.verify(password, record['password']):
            raise CustomHTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=jsonable_encoder(
                    BaseResponseModel(
                        info=[InfoModel(
                            type='error', message='Incorrect password'
                        )]
                    )
                )
            )

    @classmethod
    async def get_user_devices(cls, user_id, is_admin):
        join_condition = user \
            .outerjoin(delegation, user.c.id == delegation.c.user_id) \
            .outerjoin(responsibility, delegation.c.profile_id == responsibility.c.profile_id)\
            .outerjoin(device_group, responsibility.c.group_id == device_group.c.group_id)
        query = select([device_group.c.device_id.label('device_id')]) \
            .select_from(join_condition).distinct()
        if not is_admin:
            query = query.where(user.c.id == user_id)
        return await database.fetch_all(query)
