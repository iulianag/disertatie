from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette import status

from app_management import app
from src.utils.sensors_management import SensorsManagement
from src.utils.base_utils import raise_exception


@app.get('/sensors',
         tags=['Sensors'])
async def get_sensors_values():
    try:
        return await SensorsManagement.get_sensors_values()
    except Exception as e:
        raise_exception(e)


@app.put('/sensors/parameters',
         tags=['Sensors'])
async def update_sensors_parameters(item):
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(
                BaseResponseModel(
                    info=[InfoModel(
                        type='success', message='Sensors parameters updated'
                    )]
                )
            )
        )
    except Exception as e:
        raise_exception(e)

        
    