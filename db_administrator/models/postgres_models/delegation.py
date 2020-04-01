import sqlalchemy
from sqlalchemy import Column, Integer, Table

from .postgres_base import Base

metadata = sqlalchemy.MetaData()

delegations = Table(
    'delegations',
    Base.metadata,
    Column("user_id", Integer, nullable=False),
    Column("profile_id", Integer, nullable=False)
)