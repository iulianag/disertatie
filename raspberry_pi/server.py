import uvicorn
from app_management import app

from src.endpoints import sensors_routes


@app.on_event('startup')
async def startup():
    pass


@app.on_event('shutdown')
async def shutdown():
    pass


def run_app():
    uvicorn.run(app, host='0.0.0.0', port=5005)
    

if __name__ == '__main__':
    run_app()