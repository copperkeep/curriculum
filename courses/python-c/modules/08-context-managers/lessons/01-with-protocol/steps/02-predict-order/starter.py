class Tracer:
    def __enter__(self):
        print("enter")
    def __exit__(self, *exc):
        print("exit")

with Tracer():
    print("body")
