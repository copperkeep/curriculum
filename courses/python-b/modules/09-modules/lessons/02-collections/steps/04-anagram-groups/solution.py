from collections import defaultdict

def anagrams(words):
    groups = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return [g for g in groups.values() if len(g) > 1]
