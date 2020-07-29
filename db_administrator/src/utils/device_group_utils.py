from src.validation_models.base_validation_model import BaseResponseModel


def format_device_group_details(record):
    return {
        'device_id': record['device_id'],
        'devicename': record['devicename'],
        'group_id': record['group_id'],
        'groupname': record['groupname']
    }


def get_device_group_list(record_list):
    device_group_list = []
    for record in record_list:
        device_group_list.append(format_device_group_details(record))
    return BaseResponseModel(data=device_group_list)
