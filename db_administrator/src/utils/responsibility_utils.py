from src.validation_models.base_validation_model import BaseResponseModel


def get_profile_id_list(record_list):
    id_list = []
    for record in record_list:
        id_list.append(record['profile_id'])
    return id_list


def format_profile_group_details(record):
    return {
        'profile_id': record['profile_id'],
        'profilename': record['profilename'],
        'group_id': record['group_id'],
        'groupname': record['groupname']
    }


def get_profile_group_list(record_list):
    device_group_list = []
    for record in record_list:
        device_group_list.append(format_profile_group_details(record))
    return BaseResponseModel(data=device_group_list)
