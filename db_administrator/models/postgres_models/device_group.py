import sqlalchemy
from sqlalchemy import Column, Integer, Table

from .postgres_base import Base

metadata = sqlalchemy.MetaData()

device_group = Table(
    'device_group',
    Base.metadata,
    Column("device_id", Integer, nullable=False),
    Column("group_id", Integer, nullable=False)
)