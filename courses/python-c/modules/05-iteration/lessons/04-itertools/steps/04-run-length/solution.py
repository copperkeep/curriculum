from itertools import groupby

def rle(text):
    return "".join(f"{ch}{len(list(group))}" for ch, group in groupby(text))
