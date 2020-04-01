import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models.postgres_models.postgres_base import Base

DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/disertatie"
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def create_metadata():
    from models.postgres_models.user import users  # pylint:disable=unused-import
    from models.postgres_models.profile import profiles  # pylint:disable=unused-import
    from models.postgres_models.delegation import delegations  # pylint:disable=unused-import
    from models.postgres_models.device import devices  # pylint:disable=unused-import
    from models.postgres_models.types import types  # pylint:disable=unused-import
    from models.postgres_models.groups import groups  # pylint:disable=unused-import
    from models.postgres_models.device_group import device_group  # pylint:disable=unused-import
    from models.postgres_models.responsibility import responsibilities  # pylint:disable=unused-import
    Base.metadata.create_all(engine)



