def count_vowels(text):
    n = 0
    for ch in text:
        if ch in "aeiou":
            n = n + 1
        return n
