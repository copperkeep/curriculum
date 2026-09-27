def snake(title):
    words = []
    for word in title.split():
        words.append(word.lower())
    return "_".join(words)
