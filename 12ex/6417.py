def counter(n):
    lst = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    return len(lst) == 0


for i in range(100, 500):
    s = '0' + 50 * '2' + i * '1' + '0'
    while '00' not in s:
        s = s.replace('02', '101')
        s = s.replace('11', '2')
        s = s.replace('012', '30')
        s = s.replace('010', '00')

    #sum = s.count('1') + s.count('2') * 2 + s.count('3') * 3
    if counter(sum(map(int, list(s)))):
        print(i)


# 130
# 134
# 142
# 158
# 170
# 178
# 182
# 194
# 214
# 218
# 238
# 250