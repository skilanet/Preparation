def f(n):
    a = []
    for i in range(1, round(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return set(a)


for i in range(185311, 185330):
    p = f(i)
    if len(p) == 4:
        print(i, sorted(p))
