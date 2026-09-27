from typing import Protocol, runtime_checkable

@runtime_checkable
class HasArea(Protocol):
    def area(self) -> float: ...

def total_area(things) -> float:
    return sum(t.area() for t in things if isinstance(t, HasArea))
