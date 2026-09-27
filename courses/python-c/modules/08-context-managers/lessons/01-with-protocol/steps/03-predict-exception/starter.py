class Tracer:
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        print("exit")

try:
    with Tracer():
        raise ValueError
except ValueError:
    print("caught")
