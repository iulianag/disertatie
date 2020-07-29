from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint

from src.database_models.base import Base


responsibility = Table(
    'responsibilities',
    Base.metadata,
    Column("profile_id", Integer, ForeignKey('profiles.id'), nullable=False),
    Column("group_id", Integer, ForeignKey('groups.id'), nullable=False),
    PrimaryKeyConstraint('profile_id', 'group_id', name='responsibilities_pk')
)