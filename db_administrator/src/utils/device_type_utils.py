from src.validation_models.base_validation_model import BaseResponseModel


def format_device_type_details(record):
    return {
        'id': record['id'],
        'name': record['name'],
        'description': record['description'],
        'unit': record['unit']
    }


def get_device_type_list(record_list):
    profile_list = []
    for record in record_list:
        profile_list.append(format_device_type_details(record))
    return BaseResponseModel(data=profile_list)


def get_device_type_details(record):
    return BaseResponseModel(data=[format_device_type_details(record)])