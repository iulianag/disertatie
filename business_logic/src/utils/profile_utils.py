

def get_profile_users(user_profile_list):
    profile_users_list = []
    for user_profile in user_profile_list:
        profile_users_list.append(
            {
                'user_id': user_profile['user_id'],
                'username': user_profile['username']
            }
        )
    return profile_users_list


def get_profile_groups(profile_group_list):
    profile_groups_list = []
    for user_profile in profile_group_list:
        profile_groups_list.append(
            {
                'group_id': user_profile['group_id'],
                'groupname': user_profile['groupname']
            }
        )
    return profile_groups_list
