with open("/tmp/ab.txt", "w") as f:
    f.write("a\nb\n")
with open("/tmp/ab.txt") as f:
    print(f.readlines())
