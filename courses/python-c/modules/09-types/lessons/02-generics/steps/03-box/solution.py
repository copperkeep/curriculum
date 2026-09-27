from typing import Callable

class Box[T]:
    def __init__(self, item: T):
        self.item = item

    def get(self) -> T:
        return self.item

    def map[U](self, f: Callable[[T], U]) -> "Box[U]":
        return Box(f(self.item))
