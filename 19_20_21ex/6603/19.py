def f(s, c, m):
    if s == 0:
        return c % 2 == m % 2
    elif c == m:
        return 0
    h = [f(s - 5, c + 1, m), f(s // 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1000, 1, -1):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 2:
                print(s)
                break
