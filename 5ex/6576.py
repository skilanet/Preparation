for n in range(100):
    b = bin(n)[2:]
    k = str(b.count('1') % 2)
    if n % 2 == 0:
        b = '1' + b + k
    else:
        b = b + '0' + k

    r = int(b, 2)
    if r > 100:
        print(r, n)
