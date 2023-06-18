from sys import setrecursionlimit
from functools import lru_cache

setrecursionlimit(10000)


@lru_cache(None)
def f(pos, count, fin):
    if pos > fin:
        return 0
    elif pos == fin and count <= 7:
        return 1
    elif pos == fin and count > 7:
        return 0
    else:
        return f(pos - 5, count + 1, fin) + f(pos + 2, count + 1, fin) + f(pos ** 2, count + 1, fin)


print(f(3, 0, 28))
