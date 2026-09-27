from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    qty: int = 0

    def total(self):
        return self.price * self.qty
