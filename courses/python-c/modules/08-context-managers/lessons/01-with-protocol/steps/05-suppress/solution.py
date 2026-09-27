class Ignore:
    def __init__(self, kind):
        self.kind = kind

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return exc_type is not None and issubclass(exc_type, self.kind)
