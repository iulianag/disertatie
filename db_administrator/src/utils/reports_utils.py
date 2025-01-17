
from src.validation_models.base_validation_model import BaseResponseModel


def format_alert_details(record):
    return {
        'device_id': record['device_id'],
        'name': record['name'],
        'limit': record['limit'],
        'current_value': record['current_value'],
        'alert_date': record['alert_date'],
        'unit': record['unit']
    }


def get_alert_list(record_list):
    alert_list = []
    for record in record_list:
        alert_list.append(format_alert_details(record))
    return BaseResponseModel(data=alert_list)


def format_daily_report_details(record):
    return {
        'device_id': record['device_id'],
        'name': record['name'],
        'current_value': record['current_value'],
        'report_date': record['report_date'],
        'unit': record['unit']
    }


def get_daily_report_list(record_list):
    report_list = []
    for record in record_list:
        report_list.append(format_daily_report_details(record))
    return BaseResponseModel(data=report_list)

