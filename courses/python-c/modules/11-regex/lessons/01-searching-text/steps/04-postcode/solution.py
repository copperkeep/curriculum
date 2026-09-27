import re

def valid(code):
    return re.fullmatch(r"[A-Z]{2}-\d{3}", code) is not None
