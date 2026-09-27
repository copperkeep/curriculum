a, b = [1, 3, 5], [2, 4, 6]
out = []
while a and b:
    out.append(a.pop(0) if a[0] < b[0] else b.pop(0))
print(out + a + b)
