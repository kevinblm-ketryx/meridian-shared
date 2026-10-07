"""Shared filters."""
def moving_average(xs, n):
    return [sum(xs[i:i+n]) / n for i in range(len(xs) - n + 1)]


def clamp(x, lo, hi):
    return max(lo, min(hi, x))
