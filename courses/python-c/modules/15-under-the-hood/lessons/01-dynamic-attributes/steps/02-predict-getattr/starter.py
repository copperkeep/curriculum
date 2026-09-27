class Fallback:
    def __init__(self):
        self.x = 1
    def __getattr__(self, name):
        return f"missing:{name}"

f = Fallback()
print(f.x, f.y)
