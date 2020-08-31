import uvicorn

from settings import app
from settings import SERVER_HOST, SERVER_PORT
from src.endpoints import authorization
from src.exceptions.handlers import request_validation
from fastapi.staticfiles import StaticFiles


app.include_router(authorization.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


def main():
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT, log_level='info')


if __name__ == "__main__":
    main()
