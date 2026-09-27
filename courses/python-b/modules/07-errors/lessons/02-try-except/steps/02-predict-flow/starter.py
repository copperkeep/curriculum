try:
    print("a")
    x = 1 / 0
    print("b")
except ZeroDivisionError:
    print("c")
print("d")
