def line(mark, size):
    row = ""
    for i in range(size):
        row = row + mark
    print(row)

line("#", 5)
line("=", 3)
