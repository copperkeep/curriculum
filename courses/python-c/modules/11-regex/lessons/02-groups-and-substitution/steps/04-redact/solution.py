import re

def redact(text):
    return re.sub(r"\d{4} \d{4} \d{4} (\d{4})", r"**** **** **** \1", text)
