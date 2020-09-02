from sqlalchemy import select

from settings import database
from src.database_models.daily_reports import daily_report
from src.database_models.device import device
from src.database_models.device_type import device_type


class DailyReportsTableManager(object):
    @classmethod
    async def read_reports(cls, device_id=None, report_date=None):
        join_condition = daily_report\
            .join(device, daily_report.c.device_id == device.c.id)\
            .join(device_type, device.c.type_id == device_type.c.id)
        query = select([daily_report.c.device_id.label('device_id'),
                        daily_report.c.name.label('name'),
                        daily_report.c.current_value.label('current_value'),
                        daily_report.c.report_date.label('report_date'),
                        device_type.c.unit.label('unit')])\
            .select_from(join_condition)
        if device_id:
            query = query.where(daily_report.c.device_id == device_id)
        if report_date:
            query = query.where(daily_report.c.id == report_date)
        return await database.fetch_all(query)

    @classmethod
    async def create_report(cls, schema):
        query = daily_report.insert().values(**schema.dict())
        await database.execute(query)
        return {
            **schema.dict()
        }

    @classmethod
    async def create_reports(cls, schema_list):
        for schema in schema_list:
            await cls.create_report(schema)
        return True


