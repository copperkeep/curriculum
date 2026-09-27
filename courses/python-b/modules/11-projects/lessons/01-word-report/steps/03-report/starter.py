import string

def clean(text):
    text = text.lower()
    for mark in string.punctuation:
        text = text.replace(mark, "")
    return text.split()

# Write report(text, n) returning a string with one line per word for the top n
# words: the word left-aligned in 10 characters, then the count right-aligned
# in 3. Most common first; ties in alphabetical order. Lines joined by "\n".
# report("b a b c a b", 2) -> "b           3\na           2"
