from sqlalchemy import select

from settings import database
from src.database_models.alerts import alert
from src.database_models.device import device
from src.database_models.device_type import device_type


class AlertsTableManager(object):
    @classmethod
    async def read_alerts(cls, device_id=None, alert_date=None, device_id_list=None):
        join_condition = alert\
            .join(device, alert.c.device_id == device.c.id)\
            .join(device_type, device.c.type_id == device_type.c.id)
        query = select([alert.c.device_id.label('device_id'),
                        alert.c.name.label('name'),
                        alert.c.limit.label('limit'),
                        alert.c.current_value.label('current_value'),
                        alert.c.alert_date.label('alert_date'),
                        device_type.c.unit.label('unit')])\
            .select_from(join_condition)
        if device_id_list:
            query = query.where(alert.c.device_id.in_(device_id_list))
        if device_id:
            query = query.where(alert.c.device_id == device_id)
        if alert_date:
            query = query.where(alert.c.id == alert_date)
        return await database.fetch_all(query)

    @classmethod
    async def create_alert(cls, schema):
        query = alert.insert().values(**schema.dict())
        await database.execute(query)
        return {
            **schema.dict()
        }

