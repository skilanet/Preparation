from fnmatch import fnmatch


def is_simple(n):
    a = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return len(set(a)) == 0


def f(n):
    a = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return set(a)


for i in range(10 ** 7):
    d = f(i)
    if fnmatch(str(i), '12*4*8?'):
        if len(d) == 2:
            if list(map(is_simple, d)) == [True, True]:
                if is_simple(sum(d)):
                    print(i, sum(d))
