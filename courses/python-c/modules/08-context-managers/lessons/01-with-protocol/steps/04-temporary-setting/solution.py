settings = {"debug": False}

class Setting:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __enter__(self):
        self.old = settings[self.key]
        settings[self.key] = self.value
        return self

    def __exit__(self, *exc):
        settings[self.key] = self.old
