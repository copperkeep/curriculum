def letter_counts(text):
    counts = {}
    for ch in text:
        if ch == " ":
            continue
        counts[ch] = counts.get(ch, 0) + 1
    return counts
