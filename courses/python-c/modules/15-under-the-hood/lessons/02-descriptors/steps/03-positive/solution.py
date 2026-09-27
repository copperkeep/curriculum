class Positive:
    def __set_name__(self, owner, name):
        self.private = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.private, value)

class Box:
    width = Positive()
    height = Positive()

    def __init__(self, width, height):
        self.width = width
        self.height = height
