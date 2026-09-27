import io
from contextlib import redirect_stdout

def captured(func):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func()
    return buffer.getvalue()
