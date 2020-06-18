from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import DateTime

from src.database_models.base import Base

group = Table(
    'groups',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("groupname", String, nullable=False, unique=True),
    Column("description", String, nullable=False)
)