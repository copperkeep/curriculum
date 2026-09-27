def initials(names: list[str], sep: str = "") -> str:
    return sep.join(n[0] for n in names)
