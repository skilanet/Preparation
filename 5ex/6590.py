for n in range(10000):
    b = bin(n)[2:]
    if b.count('1') % 4 == 0:
        b = '10' + b
    else:
        b = '11' + b
    if b.count('1') % 2 == 1:
        b += '1'
    else:
        b += '0'

    r = int(b, 2)
    if r < 250:
        print(n)
