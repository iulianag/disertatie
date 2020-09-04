from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET', 'PUT', 'DELETE'],
    allow_headers=['*']
)

BL_HOST = '192.168.100.7'
BL_PORT = 5002
BL_SERVER_URL = f"http://{BL_HOST}:{BL_PORT}"