def gen():
    print("start")
    yield 1
    yield 2

g = gen()
for x in g:
    print(x)
