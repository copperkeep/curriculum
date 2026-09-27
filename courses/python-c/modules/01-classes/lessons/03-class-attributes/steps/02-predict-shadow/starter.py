class C:
    x = 1

a, b = C(), C()
a.x = 2
print(a.x, b.x, C.x)
