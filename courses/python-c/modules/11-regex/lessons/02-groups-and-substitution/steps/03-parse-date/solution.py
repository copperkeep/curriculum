import re

def parse_date(text):
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
    if m is None:
        return None
    return tuple(int(g) for g in m.groups())
