import sqlalchemy
from sqlalchemy import Column, Integer, String, Table, DateTime

from .postgres_base import Base

metadata = sqlalchemy.MetaData()

groups = Table(
    'groups',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("groupname", String, nullable=False),
    Column("description", String, nullable=False),
    Column("creation_date", DateTime, nullable=True)
)