from sqlalchemy import Column, Integer, String, Table, DateTime

from src.database_models.base import Base

user = Table(
    'users',
    Base.metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("username", String, nullable=False, unique=True),
    Column("full_name", String, nullable=False),
    Column("password", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("session_token", String, nullable=True),
    Column("login_date", DateTime, nullable=True)
)
