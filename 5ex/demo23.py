a = []
for n in range(10000):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'

    r = int(b, 2)
    if r > 40:
        a.append(n)

print(min(a))
