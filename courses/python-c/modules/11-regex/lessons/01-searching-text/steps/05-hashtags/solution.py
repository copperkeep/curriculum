import re

def hashtags(text):
    return [tag[1:] for tag in re.findall(r"#\w+", text)]
