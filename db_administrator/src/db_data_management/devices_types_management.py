from sqlalchemy import select

from settings import database
from src.db_data_management.base_management import BaseManager
from src.database_models.device import device
from src.database_models.device_type import device_type


class DevicesTypesTableManager(BaseManager):
    @classmethod
    async def read_types_devices(cls):
        join_condition = device_type\
            .join(device, device_type.c.id == device_type.c.type_id)
        query = select([device_type.c.id.label('type_id'),
                        device_type.c.name.label('typename'),
                        device.c.id.label('device_id'),
                        device.c.name.label('devicename')])\
            .select_from(join_condition)
        return await database.fetch_all(query)
