def make_counter(start=0):
    count = start
    def next_value():
        nonlocal count
        count += 1
        return count
    return next_value
