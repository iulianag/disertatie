from src.validation_models.base_validation_model import BaseResponseModel


def format_group_details(record):
    return {
        'id': record['id'],
        'groupname': record['name'],
        'description': record['description']
    }


def get_groups_list(record_list):
    group_list = []
    for record in record_list:
        group_list.append(format_group_details(record))
    return BaseResponseModel(data=group_list)


def get_group_details(record):
    return BaseResponseModel(data=[format_group_details(record)])