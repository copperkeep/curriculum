def describe(name, **info):
    parts = []
    for key in info:
        parts.append(key + "=" + str(info[key]))
    return name + ": " + ", ".join(parts)
