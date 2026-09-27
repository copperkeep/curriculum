def insertion_sort(xs):
    for i in range(1, len(xs)):
        j = i
        while j > 0 and xs[j - 1] > xs[j]:
            xs[j - 1], xs[j] = xs[j], xs[j - 1]
            j -= 1
    return xs
