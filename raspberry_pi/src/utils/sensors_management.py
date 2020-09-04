from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette import status
import json
import os

from src.scripts.dhtXX import DhtXX
from src.scripts.soil_moisture import SoilMoisture
from src.validation_models.base_validation_model import InfoModel, BaseResponseModel


class SensorsManagement(object):
    @classmethod
    async def get_sensors_values(cls):
        sensors_values = []
        with open(os.getcwd() + '/src/constants/sensors_mapping.json') as f:
            available_sensors = json.load(f)
            for sensor_id in available_sensors.keys():
                if available_sensors[sensor_id]['type'] == 'dht':
                    sensor = DhtXX(
                                model_number=available_sensors[sensor_id]['model'],
                                pin=available_sensors[sensor_id]['pin']
                            )
                    sensors_values.append(
                        {
                            'id': sensor_id,
                            'values': sensor.get_values()
                        }
                    )
                elif available_sensors[sensor_id]['type'] == 'soil_moisture':
                    sensor = SoilMoisture(
                                bus=0,
                                device=available_sensors[sensor_id]['device'],
                                channel=available_sensors[sensor_id]['channel']
                            )
                    sensors_values.append(
                        {
                            'id': sensor_id,
                            'values': sensor.get_values()
                        }
                    )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(BaseResponseModel(data=sensors_values))
        )
        
    @classmethod
    async def get_sensors_details(cls):
        sensors_values = []
        with open(os.getcwd() + '/src/constants/sensors_mapping.json') as f:
            available_sensors = json.load(f)
            for sensor_id in available_sensors.keys():
                values = []
                if available_sensors[sensor_id]['type'] == 'dht':
                    sensor = DhtXX(
                                model_number=available_sensors[sensor_id]['model'],
                                pin=available_sensors[sensor_id]['pin']
                            )
                    values = sensor.get_values()
                elif available_sensors[sensor_id]['type'] == 'soil_moisture':
                    sensor = SoilMoisture(
                                bus=0,
                                device=available_sensors[sensor_id]['device'],
                                channel=available_sensors[sensor_id]['channel']
                            )
                    values = sensor.get_values()
                for key, value in values.items():
                    sensors_values.append(
                        {
                            'id': sensor_id,
                            'parameter': key,
                            'limit': available_sensors[sensor_id]['limit'],
                            'value': value
                        }
                    )
        return sensors_values