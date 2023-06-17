import sys
from functools import lru_cache

sys.setrecursionlimit(10000)


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * f(n - 1)


print(f(2023) / f(2020))
