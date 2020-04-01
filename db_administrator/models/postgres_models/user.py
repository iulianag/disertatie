import sqlalchemy
from sqlalchemy import Column, Integer, String, Table, DateTime

from .postgres_base import Base

metadata = sqlalchemy.MetaData()

users = Table(
    'users',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("username", String, nullable=False),
    Column("full_name", String, nullable=False),
    Column("password", String, nullable=False),
    Column("email", String, nullable=False),
    Column("session_token", String, nullable=True),
    Column("login_date", DateTime, nullable=True)
)