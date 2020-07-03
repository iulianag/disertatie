from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from src.database_models.base import Base


device = Table(
    'devices',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("description", String, nullable=False),
    Column("limit", Float, nullable=False),
    Column("type_id", Integer, ForeignKey('device_types.id'), nullable=False),
    Column("added_date", DateTime, nullable=False)
)