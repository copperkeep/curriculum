from collections.abc import Iterable

def longest(words: Iterable[str]) -> str:
    best = ""
    for w in words:
        if len(w) > len(best):
            best = w
    return best
