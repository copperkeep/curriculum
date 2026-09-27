event = {"type": "click", "x": 3, "y": 4, "button": "left"}
match event:
    case {"type": "click", "x": x, "y": y}:
        print("click at", x, y)
    case _:
        print("no match")
