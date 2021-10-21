import re

def check_phone_number_is_valid(pn: str) -> bool:
    pattern = r'[0-9]{3}-[0-9]{3}-[0-9]{3}$'

    if re.match(pattern, pn):
        return True
    else:
        return False
