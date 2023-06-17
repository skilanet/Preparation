from itertools import product

a = 'ЕСТЕСТВО'
w = ['ЕЕ', 'ЕО', 'ОЕ']
k = 0

for i in product(a, repeat=8):
    s = ''.join(i)
    if all(c not in s for c in w) and (s.count('Е') + s.count('О')) >= 3 and (
            s.count('С') + s.count('Т') + s.count('В')) >= 4:
        k += 1

print(k)
