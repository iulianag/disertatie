import sqlalchemy
from sqlalchemy import Column, Integer, String, Table, DateTime

from .postgres_base import Base

metadata = sqlalchemy.MetaData()

types = Table(
    'types',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("typename", String, nullable=False),
    Column("description", String, nullable=False),
    Column("unit", String, nullable=True)
)