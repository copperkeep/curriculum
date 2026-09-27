book = {"ana": "555-0101", "bo": "555-0199"}

def lookup(name):
    return book.get(name, "unknown")

def add(name, number):
    book[name] = number
