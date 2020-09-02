import uvicorn

from settings import app
from settings import SERVER_HOST, SERVER_PORT
from src.endpoints import authorization
from src.endpoints import report
from src.endpoints import users
from src.endpoints import profiles
from src.endpoints import groups
from src.endpoints import device_types
from src.exceptions.handlers import request_validation
from fastapi.staticfiles import StaticFiles


app.include_router(authorization.router)
app.include_router(report.router)
app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(groups.router)
app.include_router(device_types.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


def main():
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT, log_level='info')


if __name__ == "__main__":
    main()
