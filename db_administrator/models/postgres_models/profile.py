import sqlalchemy
from sqlalchemy import Column, Integer, String, Table

from .postgres_base import Base

metadata = sqlalchemy.MetaData()

profiles = Table(
    'profiles',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("profilename", String, nullable=False),
    Column("description", String, nullable=False)
)