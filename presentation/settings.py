from fastapi import FastAPI
from fastapi.templating import Jinja2Templates


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5010

BL_SERVER_HOST = "localhost"
BL_SERVER_PORT = 5002
BL_SERVER_URL = f"http://{BL_SERVER_HOST}:{BL_SERVER_PORT}"

app = FastAPI()
templates = Jinja2Templates(directory="templates/")
