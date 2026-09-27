from enum import Enum

class Light(Enum):
    RED = "red"
    GREEN = "green"

g = Light("green")
print(g.name, g.value)
