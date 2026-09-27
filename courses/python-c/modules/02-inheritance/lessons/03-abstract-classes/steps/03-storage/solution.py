from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, key, value): ...

    @abstractmethod
    def load(self, key): ...

class MemoryStorage(Storage):
    def __init__(self):
        self._data = {}

    def save(self, key, value):
        self._data[key] = value

    def load(self, key):
        return self._data[key]
