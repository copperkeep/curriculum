class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def describe(self):
        return f"{self.wheels} wheels"

# Write Car(Vehicle) with an extra seats attribute. Car(5).describe() gives
# "4 wheels, 5 seats". Use super() in both __init__ and describe.
