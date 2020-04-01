import sqlalchemy
from sqlalchemy import Column, Integer, Table

from .postgres_base import Base

metadata = sqlalchemy.MetaData()

responsibilities = Table(
    'responsibilities',
    Base.metadata,
    Column("profile_id", Integer, nullable=False),
    Column("group_id", Integer, nullable=False)
)