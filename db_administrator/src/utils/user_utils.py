
from src.validation_models.base_validation_model import BaseResponseModel


def format_user_details(record):
    return {
        'id': record['id'],
        'username': record['username'],
        'full_name': record['full_name'],
        'email': record['email'],
        'login_date': record.get('login_date', None)
    }


def get_users_list(record_list):
    user_list = []
    for record in record_list:
        user_list.append(format_user_details(record))
    return BaseResponseModel(data=user_list)


def get_user_details(record):
    return BaseResponseModel(data=[format_user_details(record)])


def get_user_device_id_list(record_list):
    return [record['device_id'] for record in record_list]
