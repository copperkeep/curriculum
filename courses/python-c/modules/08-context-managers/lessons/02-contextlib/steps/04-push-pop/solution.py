from contextlib import contextmanager

@contextmanager
def pushed(stack, item):
    stack.append(item)
    try:
        yield stack
    finally:
        stack.pop()
