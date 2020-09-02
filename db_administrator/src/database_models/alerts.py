from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Float, DateTime
from sqlalchemy import ForeignKey

from src.database_models.base import Base


alert = Table(
    'alerts',
    Base.metadata,
    Column("device_id", Integer, ForeignKey('devices.id'), nullable=False),
    Column("name", String, nullable=False),
    Column("limit", Float, nullable=False),
    Column("current_value", Float, nullable=False),
    Column("alert_date", DateTime, nullable=False)
)
