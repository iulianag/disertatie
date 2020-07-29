from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint

from src.database_models.base import Base


device_group = Table(
    'device_group',
    Base.metadata,
    Column("device_id", Integer, ForeignKey('devices.id'), nullable=False),
    Column("group_id", Integer, ForeignKey('groups.id'), nullable=False),
    PrimaryKeyConstraint('device_id', 'group_id', name='device_group_pk')
)