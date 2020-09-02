from src.validation_models.base_validation_model import BaseResponseModel


def format_sensor_details(rpi_sensor_details, db_sensor_details):
    return {
        'id': db_sensor_details['id'],
        'name': db_sensor_details['name'],
        'type': rpi_sensor_details['type'],
        'value': rpi_sensor_details['value']
    }


def get_sensors_values(rpi_values, db_values):
    sensors_details = []
    for key, value in rpi_values.items():
        db_value = db_values.get(key, None)
        if db_value:
            for k, v in value.items():
                sensors_details.append(
                    format_sensor_details(
                        {'type': k, 'value': v},
                        db_value
                    )
                )
    return BaseResponseModel(data=sensors_details)
