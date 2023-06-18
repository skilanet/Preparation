import sys, functools

sys.setrecursionlimit(10000)


@functools.lru_cache(None)
def counter(n, f):
    if n > f:
        return 0
    elif n == f:
        return 1
    else:
        return counter(n + 3, f) + counter(n + 5, f) + counter(n * 2, f)


print(str(counter(1, 3000) + counter(3000, 4999) + counter(5001, 10000) + counter(1, 2999) + counter(3001, 5000) + counter(
    5000, 10000))[::-1])


