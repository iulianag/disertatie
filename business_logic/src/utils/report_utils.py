from src.validation_models.base_validation_model import BaseResponseModel
from datetime import datetime
from src.validation_models.report_model import AlertModel


def format_sensor_details(rpi_sensor_details, db_sensor_details):
    return {
        'id': db_sensor_details['id'],
        'name': db_sensor_details['name'],
        'type': rpi_sensor_details['type'],
        'value': rpi_sensor_details['value']
    }


def get_sensors_values(rpi_values_list, db_values):
    sensors_details = []
    db_devices = []
    for value in db_values:
        db_devices.append(value['id'])
    for rpi_values in rpi_values_list:
        if rpi_values['id'] in db_devices:
            sensors_details.append(
                format_sensor_details(rpi_values, db_values[db_devices.index(rpi_values['id'])])
            )
    return BaseResponseModel(data=sensors_details)


def format_alert_details(rpi_sensor_details):
    return {
        'device_id': rpi_sensor_details['id'],
        'name': rpi_sensor_details['parameter'],
        'limit': rpi_sensor_details['limit'],
        'current_value': rpi_sensor_details['value']
    }


def get_alert_value(rpi_values, db_values):
    sensors_details = []
    db_devices = []
    for value in db_values:
        db_devices.append(value['id'])
    if rpi_values['id'] in db_devices:
        sensors_details.append(
            format_alert_details(rpi_values)
        )
    return BaseResponseModel(data=sensors_details)


def format_report_details(rpi_sensor_details):
    return {
        'device_id': rpi_sensor_details['id'],
        'name': rpi_sensor_details['parameter'],
        'current_value': rpi_sensor_details['value']
    }


def get_report_values(rpi_values_list, db_values):
    sensors_details = []
    db_devices = []
    for value in db_values:
        db_devices.append(value['id'])
    for rpi_values in rpi_values_list:
        rpi_values_json = rpi_values.dict()
        if rpi_values_json['id'] in db_devices:
            sensors_details.append(
                format_report_details(rpi_values_json)
            )
    return BaseResponseModel(data=sensors_details)
