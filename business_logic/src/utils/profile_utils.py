

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
