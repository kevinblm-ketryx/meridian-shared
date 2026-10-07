def moving_average(xs, n):
    return [sum(xs[i:i+n]) / n for i in range(len(xs) - n + 1)]
