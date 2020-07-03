from sqlalchemy import and_, or_
import datetime

from settings import database
from src.db_data_management.base_management import BaseManager
from src.database_models.user import user


class UsersTableManager(BaseManager):
    @classmethod
    async def is_valid_token(cls, token):
        login_date_limit = datetime.datetime.utcnow() - datetime.timedelta(minutes=60)
        query = user.select().where(and_(user.c.session_token == token,
                                         user.c.login_date > login_date_limit))
        user_details = await database.fetch_one(query)
        if not user_details:
            return False
        extend_session_query = user.update()\
            .where(user.c.session_token == token)\
            .values({user.c.login_date: datetime.datetime.utcnow()})
        await database.execute(extend_session_query)
        return user_details['id']

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