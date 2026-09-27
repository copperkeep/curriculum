import functools

def positive_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if any(a < 0 for a in args):
            raise ValueError("arguments must not be negative")
        return func(*args, **kwargs)
    return wrapper
