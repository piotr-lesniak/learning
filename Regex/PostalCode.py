import re


def validate_postal_code(postal: str) -> bool:
    postal_to_validate = postal
    pattern = r'[0-9]{2}-[0-9]{3}$'

    if re.match(pattern, postal):
        return True
    else:
        return False
