from fastapi import FastAPI
import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from src.database_models.base import Base

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001

app = FastAPI()

DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1:5432/disertatie"
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def create_metadata():
    Base.metadata.create_all(engine)



