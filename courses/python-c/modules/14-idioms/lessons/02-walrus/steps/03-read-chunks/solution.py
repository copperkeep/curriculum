def batches(data, size):
    out = []
    while batch := data[:size]:
        out.append(batch)
        data = data[size:]
    return out
