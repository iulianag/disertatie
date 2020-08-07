from fastapi import status
from fastapi.encoders import jsonable_encoder

from settings import database
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.db_data_management.base_management import BaseManager
from src.database_models.device_type import device_type


class DevicesTableManager(BaseManager):
    @classmethod
    async def read_all_records(cls, table, filter_query=None, type_name=None):
        query = table.select()
        if filter_query:
            query = query.where(table.c.name.ilike(f'%{filter_query}%'))
        if type_name:
            type_query = device_type.select().where(device_type.c.name == type_name)
            type_record = await database.fetch_one(type_query)
            if not type_record:
                raise CustomHTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    content=jsonable_encoder(
                        BaseResponseModel(
                            info=[InfoModel(
                                type='error', message='Type not found'
                            )]
                        )
                    )
                )
            query = query.where(table.c.type_id == type_record['id'])
        return await database.fetch_all(query)
