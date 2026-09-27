counts = {}
for ch in "aba":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
