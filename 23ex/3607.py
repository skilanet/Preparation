def counter(n, f):
    if n > f:
        return 0
    elif n == f:
        return 1
    else:
        return counter(n + 2, f) + counter(n * 5, f)


print(counter(2, 50))
