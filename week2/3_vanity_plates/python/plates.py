import re


def is_valid(s: str) -> bool:
    s = s.strip()

    # Maximum of 6 characters and a minimum of 2 characters
    if len(s) > 6 or len(s) < 2:
        return False

    # All vanity plates must start (^) with at least two letters
    # Numbers cannot be used in the middle of a plate; they must come at the end ($)
    # No periods, spaces, or punctuation marks are allowed
    # The first number used cannot be a '0'
    if not re.fullmatch(r'^[A-Z]{2,}[^\s0]\d+$', s):
        return False

    return True

def plates(s: str) -> str:
    return 'Valid' if is_valid(s) else 'Invalid'