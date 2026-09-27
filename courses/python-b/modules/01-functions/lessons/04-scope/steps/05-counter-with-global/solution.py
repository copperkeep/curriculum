calls = 0

def ping():
    global calls
    calls = calls + 1
    return "pong"

ping()
ping()
ping()
