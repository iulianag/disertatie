

def get_profile_id_list(record_list):
    id_list = []
    for record in record_list:
        id_list.append(record['profile_id'])
    return id_list
