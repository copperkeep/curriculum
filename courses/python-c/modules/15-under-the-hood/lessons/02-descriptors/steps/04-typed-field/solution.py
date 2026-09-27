class Typed:
    def __init__(self, kind):
        self.kind = kind

    def __set_name__(self, owner, name):
        self.private = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private)

    def __set__(self, obj, value):
        if not isinstance(value, self.kind):
            raise TypeError(f"expected {self.kind.__name__}")
        setattr(obj, self.private, value)

class Person:
    name = Typed(str)
    age = Typed(int)

    def __init__(self, name, age):
        self.name = name
        self.age = age
