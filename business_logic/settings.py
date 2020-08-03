from fastapi import FastAPI


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5002

DB_SERVER_HOST = "localhost"
DB_SERVER_PORT = 5001
DB_SERVER_URL = f"http://{DB_SERVER_HOST}:{DB_SERVER_PORT}"

app = FastAPI()
