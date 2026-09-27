log = []

def parse(text):
    try:
        n = int(text)
    except ValueError:
        return None
    else:
        return n
    finally:
        log.append(text)
