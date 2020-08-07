

def get_group_devices(group_device_list):
    group_devices_list = []
    for user_profile in group_device_list:
        group_devices_list.append(
            {
                'device_id': user_profile['device_id'],
                'devicename': user_profile['devicename']
            }
        )
    return group_devices_list


def get_group_profiles(group_profile_list):
    group_profiles_list = []
    for user_profile in group_profile_list:
        group_profiles_list.append(
            {
                'profile_id': user_profile['profile_id'],
                'profilename': user_profile['profilename']
            }
        )
    return group_profiles_list
