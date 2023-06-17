n = 25
b = bin(n)[2:]
k = str(b.count('1') % 2)
if n % 2 == 0:
    b = '1' + b + k
else:
    b = b + '0' + k

r = int(b, 2)
print(r)