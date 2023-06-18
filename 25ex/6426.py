from fnmatch import fnmatch


def divs(n):
    a = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return set(a)


def is_simple(n):
    a = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return len(set(a)) == 0


for i in range(311, 10 ** 8, 311):
    d = divs(i)
    if fnmatch(str(i), '12?5*5??'):
        if list(map(is_simple, d)) == [True, True]:
            print(i, i // 331)