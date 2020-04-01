import uvicorn
from base import app
from models.postgres_management import database, create_metadata
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000


@app.on_event("startup")
async def startup():
    await database.connect()
    await create_metadata()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


def main():
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT, log_level='info')


if __name__ == "__main__":
    main()