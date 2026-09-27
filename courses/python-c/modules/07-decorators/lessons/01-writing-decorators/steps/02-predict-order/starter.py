def announce(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@announce
def hi():
    print("hi")

hi()
