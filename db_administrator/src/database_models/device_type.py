from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table

from src.database_models.base import Base

device_type = Table(
    'device_types',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("typename", String, nullable=False, unique=True),
    Column("description", String, nullable=False),
    Column("unit", String, nullable=True)
)