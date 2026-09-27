def ratio(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"
    except TypeError:
        return "not a number"
