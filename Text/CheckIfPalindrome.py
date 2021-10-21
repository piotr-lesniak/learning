def check_if_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    else:
        return False
