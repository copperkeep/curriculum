class Evens:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return iter(range(0, self.limit, 2))
