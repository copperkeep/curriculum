from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "o"

class Square:
    def draw(self) -> str:
        return "[]"

def render(items: list[Drawable]) -> str:
    return " ".join(item.draw() for item in items)
