from itertools import product, permutations

k = 0
for i in product('матвей', repeat=6):
    s = ''.join(i)
    if 'ае' not in s and s[0] != 'й' and s.count('м') == 1 and s.count('а') == 1 \
            and s.count('т') == 1 and s.count('в') == 1\
            and s.count('е') == 1 and s.count('й') == 1:
        k += 1

print(k)
