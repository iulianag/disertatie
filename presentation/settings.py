from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5010

BL_SERVER_HOST = "localhost"
BL_SERVER_PORT = 5002
BL_SERVER_URL = f"http://{BL_SERVER_HOST}:{BL_SERVER_PORT}"

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
