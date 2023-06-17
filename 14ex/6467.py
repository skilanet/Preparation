for p in range(8, 1000):
    for y in range(100):
        for x in range(100):
            if (7 * p + 1) * (5 * p + 7) == x*(p**2) + y*p + 7:
                print(y*p**2 + x*p)

