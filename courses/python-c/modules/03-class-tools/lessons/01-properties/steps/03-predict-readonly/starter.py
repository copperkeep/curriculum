class Sq:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

s = Sq(2)
s.area = 5
