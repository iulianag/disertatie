from src.validation_models.base_validation_model import BaseResponseModel


def format_device_details(record):
    return {
        'id': record['id'],
        'name': record['name'],
        'description': record['description'],
        'limit': record['limit'],
        'type_id': record['type_id']
    }


def get_device_list(record_list):
    profile_list = []
    for record in record_list:
        profile_list.append(format_device_details(record))
    return BaseResponseModel(data=profile_list)


def get_device_details(record):
    return BaseResponseModel(data=[format_device_details(record)])