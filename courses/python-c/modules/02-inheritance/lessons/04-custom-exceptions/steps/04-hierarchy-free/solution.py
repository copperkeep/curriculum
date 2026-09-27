class ParseError(Exception):
    pass

class EmptyInput(ParseError):
    pass

class BadNumber(ParseError):
    pass

def parse(text):
    if not text.strip():
        raise EmptyInput()
    try:
        return int(text)
    except ValueError:
        raise BadNumber(text) from None
