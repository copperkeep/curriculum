from collections import Counter

def top_words(text, n):
    return Counter(text.lower().split()).most_common(n)
