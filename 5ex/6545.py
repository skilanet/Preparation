def rev(n):
    return n + int(str(n)[::-1])


def check(s):
    return str(s) == str(s)[::-1]


k = 0
for n in range(100, 201):
    r = n
    for j in range(5):
        r = rev(r)
        if check(r):
            k += 1
            break

print(k)
