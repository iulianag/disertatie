from src.validation_models.base_validation_model import BaseResponseModel


def get_user_profile_id_list(record_list):
    id_list = []
    for record in record_list:
        id_list.append(record['profile_id'])
    return id_list


def format_delegation_details(record):
    return {
        'user_id': record['user_id'],
        'username': record['username'],
        'profile_id': record['profile_id'],
        'profilename': record['profilename']
    }


def get_delegations_list(record_list):
    user_list = []
    for record in record_list:
        user_list.append(format_delegation_details(record))
    return BaseResponseModel(data=user_list)


def get_delegation_details(record):
    return BaseResponseModel(data=[format_delegation_details(record)])
