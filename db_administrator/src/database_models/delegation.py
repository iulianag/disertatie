from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import PrimaryKeyConstraint

from src.database_models.base import Base


delegation = Table(
    'delegations',
    Base.metadata,
    Column("user_id", Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    Column("profile_id", Integer, ForeignKey('profiles.id', ondelete='CASCADE'), nullable=False),
    PrimaryKeyConstraint('user_id', 'profile_id', name='delegations_pk')
)
