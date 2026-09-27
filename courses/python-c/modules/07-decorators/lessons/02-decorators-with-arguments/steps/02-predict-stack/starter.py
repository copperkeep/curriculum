def tag(t):
    def decorator(func):
        def wrapper():
            return f"<{t}>{func()}</{t}>"
        return wrapper
    return decorator

@tag("b")
@tag("i")
def hi():
    return "hi"

print(hi())
