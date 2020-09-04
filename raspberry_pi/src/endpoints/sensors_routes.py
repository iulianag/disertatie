from fastapi.encoders import jsonable_encoder
from fastapi import Security, status
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
import requests

from app_management import app
from src.utils.sensors_management import SensorsManagement
from src.utils.base_utils import raise_exception
from app_management import BL_SERVER_URL
from src.validation_models.base_validation_model import BaseResponseModel, InfoModel


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

        
@app.post('/alerts',
         tags=['Reports'])
async def post_alerts():
    try:
        authenticated = requests.post(
                f"{BL_SERVER_URL}/login",
                json={'username': 'admin', 'password': 'useradmin'}
            )
        if authenticated.status_code == status.HTTP_200_OK:
            sensors_values = await SensorsManagement.get_sensors_details()
            for sensor in sensors_values:
                if (sensor['value'] - 1) < sensor['limit'] or (sensor['value'] + 1) > sensor['limit']:
                    response = requests.post(
                        f"{BL_SERVER_URL}/alerts",
                        headers={"Authorization": (authenticated.json())['data'][0]['token']},
                        json=sensor
                    )
            authenticated = requests.post(
                f"{BL_SERVER_URL}/logout",
                headers={"Authorization": (authenticated.json())['data'][0]['token']}
            )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(
                    BaseResponseModel(
                        info=[InfoModel(
                            type='success', message='Sensors were verified'
                        )]
                    )
                )
            )
        return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=jsonable_encoder(
                    BaseResponseModel(
                        info=[InfoModel(
                            type='error', message='Internal server error'
                        )]
                    )
                )
            )
    except Exception as e:
        raise_exception(e)
    
    
@app.post('/reports',
         tags=['Reports'])
async def post_daily_reports():
    try:
        authenticated = requests.post(
                f"{BL_SERVER_URL}/login",
                json={'username': 'admin', 'password': 'useradmin'}
            )
        if authenticated.status_code == status.HTTP_200_OK:
            sensors_values = await SensorsManagement.get_sensors_details()
            reports_list = []
            for sensor in sensors_values:
                reports_list.append(
                        {
                            'id': sensor['id'],
                            'parameter': sensor['parameter'],
                            'value': sensor['value']
                        }
                    )
            response = requests.post(
                f"{BL_SERVER_URL}/reports",
                headers={"Authorization": (authenticated.json())['data'][0]['token']},
                json=reports_list
            )
            authenticated = requests.post(
                f"{BL_SERVER_URL}/logout",
                headers={"Authorization": (authenticated.json())['data'][0]['token']}
            )
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(
                    BaseResponseModel(
                        info=[InfoModel(
                            type='success', message='Daily reports created'
                        )]
                    )
                )
            )
        return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content=jsonable_encoder(
                    BaseResponseModel(
                        info=[InfoModel(
                            type='error', message='Internal server error'
                        )]
                    )
                )
            )
    except Exception as e:
        raise_exception(e)
    