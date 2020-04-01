import sqlalchemy
from sqlalchemy import Column, Integer, String, Table, DateTime, Float

from .postgres_base import Base

metadata = sqlalchemy.MetaData()

devices = Table(
    'devices',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("devicename", String, nullable=False),
    Column("description", String, nullable=False),
    Column("limit", Float, nullable=False),
    Column("type_id", Integer, nullable=False),
    Column("added_date", DateTime, nullable=True)
)