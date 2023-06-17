from functools import reduce


def f(n):
    a = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return set(a)


def mult(m, n):
    return m * n


for i in range(174457, 174505):
    p = f(i)
    if len(p) == 2:
        print(i, p, reduce(mult, p))
