class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def cost(self):
        return self.price

class Discounted(Item):
    def __init__(self, name, price, percent):
        self.name = name
        self.price = price
        self.percent = percent

    def cost(self):
        return self.price * (100 - self.percent) / 100

def total_cost(items):
    return sum(item.cost() for item in items)
