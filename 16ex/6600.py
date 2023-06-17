from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)


@lru_cache(None)
def f(n):
    if n >= 10000:
        return 1
    else:
        if n % 2 == 0:
            return f(n + 3) + 7
        else:
            return f(n + 1) - 3


print(f(50) - f(57))
