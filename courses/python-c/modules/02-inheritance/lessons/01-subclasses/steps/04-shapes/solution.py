class Shape:
    def area(self):
        raise NotImplementedError

    def describe(self):
        return f"{type(self).__name__} with area {self.area()}"

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2
