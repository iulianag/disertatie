

def get_user_profiles(user_profile_list):
    user_profiles_list = []
    for user_profile in user_profile_list:
        user_profiles_list.append(
            {
                'profile_id': user_profile['profile_id'],
                'profilename': user_profile['profilename']
            }
        )
    return user_profiles_list
