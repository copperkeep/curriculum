class Parent:
    @classmethod
    def make(cls):
        return cls()

class Child(Parent):
    pass

print(type(Child.make()).__name__)
