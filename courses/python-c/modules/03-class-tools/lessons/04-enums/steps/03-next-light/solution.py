from enum import Enum

class Light(Enum):
    RED = "red"
    GREEN = "green"
    AMBER = "amber"

def next_light(light):
    order = {Light.RED: Light.GREEN, Light.GREEN: Light.AMBER, Light.AMBER: Light.RED}
    return order[light]
