from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, key, value): ...

    @abstractmethod
    def load(self, key): ...

# Write MemoryStorage(Storage), keeping values in a dict.
