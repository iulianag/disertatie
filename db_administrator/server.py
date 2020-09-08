import uvicorn
from settings import database
from settings import create_metadata
from settings import app
from settings import SERVER_HOST, SERVER_PORT
from settings import pwd_context
from src.endpoints import authorization
from src.endpoints import users
from src.endpoints import profiles
from src.endpoints import devices
from src.endpoints import device_types
from src.endpoints import groups
from src.endpoints import delegations
from src.endpoints import device_group
from src.endpoints import respnsibilities
from src.endpoints import reports
from src.exceptions.handlers import request_validation

from src.db_data_management.users_management import UsersTableManager
from src.database_models.user import user
from src.validation_models.user_model import UserIn

from src.database_models.profile import profile
from src.db_data_management.profiles_management import ProfilesTableManager
from src.validation_models.profile_model import ProfileIn

from src.db_data_management.delegations_management import DelegationsTableManager
from src.validation_models.delegation_model import DelegationIn


app.include_router(authorization.router)
app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(devices.router)
app.include_router(device_types.router)
app.include_router(groups.router)
app.include_router(delegations.router)
app.include_router(device_group.router)
app.include_router(respnsibilities.router)
app.include_router(reports.router)


@app.on_event("startup")
async def startup():
    await database.connect()
    await create_metadata()
    if len(await UsersTableManager.read_all_records(user)) == 0:
        admin_user = await UsersTableManager.create_record(user, UserIn(username='admin',
                                                                        password=pwd_context.encrypt('useradmin'),
                                                                        full_name='Administrator user',
                                                                        email='gabor_iuliana@yahoo.com'))
        admin_profile = await ProfilesTableManager.create_record(profile, ProfileIn(name='admin',
                                                                                    description='Administrator profile'))
        await DelegationsTableManager.create_delegation(DelegationIn(user_id=admin_user['id'],
                                                                     profile_id=admin_profile['id']))


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


def main():
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT, log_level='info')


if __name__ == "__main__":
    main()
