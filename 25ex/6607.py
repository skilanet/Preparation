from fnmatch import fnmatch


def del_sum(n):
    a = []
    for i in range(1, round(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return sum(set(a))


k = 0
for i in range(500_000, 10 ** 9):
    d = del_sum(i)
    if fnmatch(str(d), '*7?'):
        print(i, d)
        k += 1
    if k == 5:
        break
