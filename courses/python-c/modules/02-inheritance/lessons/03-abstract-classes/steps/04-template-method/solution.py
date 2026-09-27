from abc import ABC, abstractmethod

class Greeter(ABC):
    @abstractmethod
    def greeting(self): ...

    def greet(self, name):
        return f"{self.greeting()}, {name}!"

class English(Greeter):
    def greeting(self):
        return "Hello"

class Spanish(Greeter):
    def greeting(self):
        return "Hola"
