for n in range(6, 20):
    if (7 ** 500 - int('53', n)) % 6 == 0:
        print(n)
        break