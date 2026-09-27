def f():
    try:
        return 1
    finally:
        print("cleanup")

print(f())
