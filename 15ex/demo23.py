def d(n, m):
    return n % m == 0


def f(x, a):
    return (d(x, 2) <= (not d(x, 3))) or (x + a >= 100)



