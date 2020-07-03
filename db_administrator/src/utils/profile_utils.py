from src.validation_models.base_validation_model import BaseResponseModel


def format_profile_details(record):
    return {
        'id': record['id'],
        'profilename': record['name'],
        'description': record['description']
    }


def get_profiles_list(record_list):
    profile_list = []
    for record in record_list:
        profile_list.append(format_profile_details(record))
    return BaseResponseModel(data=profile_list)


def get_profile_details(record):
    return BaseResponseModel(data=[format_profile_details(record)])