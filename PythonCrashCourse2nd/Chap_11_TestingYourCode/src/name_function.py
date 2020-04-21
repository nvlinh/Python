def get_formatted_name(first_name, last_name, middle_name=''):
    """Return full name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}".title()
    else:
        full_name = f"{first_name} {last_name}".title()
    return full_name

