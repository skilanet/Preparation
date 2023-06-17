from itertools import product

w = ['16', '61', '36', '63', '56', '65', '76', '67']
k = 0
for i in product('01234567', repeat=5):
    s = ''.join(i)
    if s.count('6') == 1 and all(c not in s for c in w) and s[0] != '0':
        k += 1
print(k)
