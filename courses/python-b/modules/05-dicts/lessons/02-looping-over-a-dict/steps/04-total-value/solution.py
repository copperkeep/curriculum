prices = {"pen": 2, "pad": 5, "ink": 12}
stock = {"pen": 10, "pad": 3, "ink": 1}

def worth():
    total = 0
    for item, price in prices.items():
        total = total + price * stock[item]
    return total
