from dataclasses import dataclass

@dataclass
class Circle:
    r: float

@dataclass
class Rect:
    w: float
    h: float

def area(shape):
    match shape:
        case Circle(r=r):
            return 3.14 * r * r
        case Rect(w=w, h=h):
            return w * h
        case _:
            raise ValueError("unknown shape")
