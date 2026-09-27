def describe(resp):
    match resp:
        case {"status": "ok", "data": {"user": {"name": name}}}:
            return f"Hello, {name}"
        case {"status": "error", "code": code}:
            return f"Error {code}"
        case _:
            return "Bad response"
