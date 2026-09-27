HANDLERS = {}

def register(name):
    def decorator(func):
        HANDLERS[name] = func
        return func
    return decorator
