class Settings:
    def __init__(self):
        self.theme = "light"
        self.size = 12

def apply(settings, changes):
    ignored = []
    for name, value in changes.items():
        if hasattr(settings, name):
            setattr(settings, name, value)
        else:
            ignored.append(name)
    return ignored
