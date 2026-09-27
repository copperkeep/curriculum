class Bag:
    items = []
    def add(self, x):
        self.items.append(x)

b1, b2 = Bag(), Bag()
b1.add("a")
b2.add("b")
print(b2.items)
