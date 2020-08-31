from fastapi import Security
from fastapi.security.api_key import APIKeyCookie, APIKey


async def is_authenticated(authorization: APIKey = Security(APIKeyCookie(name="Authorization", auto_error=False))):
    if authorization:
        return authorization.name
    return authorization
