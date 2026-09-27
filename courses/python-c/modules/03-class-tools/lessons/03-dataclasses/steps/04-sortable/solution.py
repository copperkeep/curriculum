from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Version:
    major: int
    minor: int
    patch: int
