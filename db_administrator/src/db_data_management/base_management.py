from fastapi import status
from fastapi.encoders import jsonable_encoder

from settings import database
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


class BaseManager(object):
    @classmethod
    async def create_record(cls, table, schema):
        query = table.insert().values(**schema.dict())
        record_id = await database.execute(query)
        return {
            'id': record_id,
            **schema.dict()
        }

    @classmethod
    async def read_record(cls, table, record_id):
        query = table.select().where(table.c.id == record_id)
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
        return record

    @classmethod
    async def read_all_records(cls, table, filter_query=None):
        query = table.select()
        if filter_query:
            query = query.where(table.c.name.ilike(f'%{filter_query}%'))
        return await database.fetch_all(query)

    @classmethod
    async def update_record(cls, table, record_id, schema):
        query = table.select().where(table.c.id == record_id)
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
        update_query = table.update().where(table.c.id == record_id).values(**schema.dict())
        await database.execute(update_query)
        return await database.fetch_one(query)

    @classmethod
    async def delete_record(cls, table, record_id):
        query = table.select().where(table.c.id == record_id)
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
        delete_query = table.delete().where(table.c.id == record_id)
        return not(bool(await database.execute(delete_query)))
