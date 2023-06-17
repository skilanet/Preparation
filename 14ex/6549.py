for p in range(100, 1000):
    q = int(str(p)[::-1])
    if 9 * (p ** 2) + 6 * (p ** 1) + 1 * (p ** 0) == 1 * (q ** 2) + 6 * (q ** 1) + 9 * (q ** 0):
        print(p)
        break