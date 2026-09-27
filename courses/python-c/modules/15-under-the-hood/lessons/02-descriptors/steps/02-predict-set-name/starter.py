class Field:
    def __set_name__(self, owner, name):
        self.name = name

class Item:
    price = Field()

print(Item.__dict__["price"].name)
