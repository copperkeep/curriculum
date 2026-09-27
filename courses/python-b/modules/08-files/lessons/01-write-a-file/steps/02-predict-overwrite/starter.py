with open("/tmp/x.txt", "w") as f:
    f.write("a")
with open("/tmp/x.txt", "w") as f:
    f.write("b")
with open("/tmp/x.txt") as f:
    print(f.read())
