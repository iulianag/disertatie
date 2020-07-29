from sqlalchemy import select
from sqlalchemy import and_
import datetime
from fastapi import status
from fastapi.encoders import jsonable_encoder

from settings import database
from src.exceptions.definitions.CustomHTTPException import CustomHTTPException
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel
from src.database_models.device_group import device_group
from src.database_models.device import device
from src.database_models.group import group


class DevicegroupTableManager(object):
    @classmethod
    async def delete_device_group(cls, device_id, group_id):
        query = device_group.select().where(and_(device_group.c.device_id == device_id,
                                                 device_group.c.group_id == group_id))
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
        delete_query = device_group.delete().where(and_(device_group.c.device_id == device_id,
                                                        device_group.c.group_id == group_id))
        return not (bool(await database.execute(delete_query)))

    @classmethod
    async def read_devices_groups(cls, device_id=None, group_id=None):
        join_condition = device\
            .join(device_group, device_group.c.device_id == device.c.id)\
            .join(group, group.c.id == device_group.c.group_id)
        query = select([device.c.id.label('device_id'),
                        device.c.name.label('devicename'),
                        group.c.id.label('group_id'),
                        group.c.name.label('groupname')])\
            .select_from(join_condition)
        if device_id:
            query = query.where(device.c.id == device_id)
        if group_id:
            query = query.where(group.c.id == group_id)
        return await database.fetch_all(query)

    @classmethod
    async def create_device_group(cls, schema):
        query = device_group.insert().values(**schema.dict())
        await database.execute(query)
        return {
            **schema.dict()
        }
