import string

def clean(text):
    text = text.lower()
    for mark in string.punctuation:
        text = text.replace(mark, "")
    return text.split()

def report(text, n):
    counts = {}
    for word in clean(text):
        counts[word] = counts.get(word, 0) + 1
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    lines = [f"{word:<10}{count:>3}" for word, count in ranked[:n]]
    return "\n".join(lines)
