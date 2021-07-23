import re


def create_initials(s):
    """
    Return the initial letter of each word in s, capitalized and strung together
    Example: John Smith -> JS
    """
    return "".join(s[0] if s else '' for s in re.split(r"[\W_]+", s)).upper()
