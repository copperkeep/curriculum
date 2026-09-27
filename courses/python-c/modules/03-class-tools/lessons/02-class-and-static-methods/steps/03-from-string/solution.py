class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, text):
        x, y = text.split(",")
        return cls(int(x), int(y))
