import string

def clean(text):
    text = text.lower()
    for mark in string.punctuation:
        text = text.replace(mark, "")
    return text.split()
