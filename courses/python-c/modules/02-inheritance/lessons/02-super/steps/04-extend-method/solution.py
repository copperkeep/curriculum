class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def describe(self):
        return f"{self.wheels} wheels"

class Car(Vehicle):
    def __init__(self, seats):
        super().__init__(4)
        self.seats = seats

    def describe(self):
        return super().describe() + f", {self.seats} seats"
