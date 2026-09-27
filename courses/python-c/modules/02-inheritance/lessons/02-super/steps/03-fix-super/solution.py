class Pet:
    def __init__(self, name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
