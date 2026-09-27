def run(line):
    match line.split():
        case ["look"]:
            return "You look around."
        case ["go", direction]:
            return f"You go {direction}."
        case ["drop", *items] if items:
            return f"Dropped {len(items)} items."
        case _:
            return "Huh?"
