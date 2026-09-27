def status(code):
    match code:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case n if 400 <= n < 500:
            return "client error"
        case n if 500 <= n < 600:
            return "server error"
        case _:
            return "unknown"
