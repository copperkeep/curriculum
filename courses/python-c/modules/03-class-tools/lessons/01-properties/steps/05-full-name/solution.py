class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full(self):
        return f"{self.first} {self.last}"

    @full.setter
    def full(self, value):
        self.first, self.last = value.split(" ", 1)
