a = []
for n in range(10, 15):
    b = bin(n)[3:]
    r = int(b, 2)
    a.append(n - r)

print(len(set(a)))
