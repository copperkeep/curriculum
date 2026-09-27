def serve(queue):
    served = []
    while queue:
        served.append(queue.pop(0))
    return served
