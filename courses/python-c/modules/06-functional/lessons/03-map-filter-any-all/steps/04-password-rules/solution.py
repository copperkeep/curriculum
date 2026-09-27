def strong(pw):
    return (
        len(pw) >= 8
        and any(ch.isdigit() for ch in pw)
        and any(ch.isupper() for ch in pw)
        and any(ch.islower() for ch in pw)
    )
