class Temp:
    def __init__(self, c):
        self.c = c

    @property
    def f(self):
        return self.c * 9 / 5 + 32

t = Temp(0)
t.c = 100
print(t.f)
