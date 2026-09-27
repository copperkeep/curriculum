class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)
