cmd = ["go", "north", 2]
match cmd:
    case ["go", direction]:
        print("move", direction)
    case ["go", direction, steps]:
        print("move", direction, steps)
    case _:
        print("unknown")
