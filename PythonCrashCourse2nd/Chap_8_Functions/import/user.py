def build_profile(first_name, last_name, **user_ino):
    """Build a dictionary of an user information"""
    user_ino['first_name'] = first_name
    user_ino['last_name'] = last_name
    return user_ino


def print_user_names(*user_names):
    """Print all username in list"""
    for user_name in user_names:
        print(user_name)

