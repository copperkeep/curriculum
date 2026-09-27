class Animal:
    def kind(self):
        return "Animal"
    def intro(self):
        return "I am a " + self.kind()

class Cat(Animal):
    def kind(self):
        return "Cat"

print(Cat().intro())
