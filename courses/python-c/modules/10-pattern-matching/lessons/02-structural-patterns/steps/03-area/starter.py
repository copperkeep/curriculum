from dataclasses import dataclass

@dataclass
class Circle:
    r: float

@dataclass
class Rect:
    w: float
    h: float

# Write area(shape) using match with class patterns. Use 3.14 for pi.
# Raise ValueError for anything else.
