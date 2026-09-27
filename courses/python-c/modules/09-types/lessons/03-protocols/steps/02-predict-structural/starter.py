from typing import Protocol, runtime_checkable

@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...

class File:
    def close(self) -> None:
        pass

print(isinstance(File(), Closable))
