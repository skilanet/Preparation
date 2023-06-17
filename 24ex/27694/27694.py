with open('27694.txt') as f:
    s = f.readline()
    k, m = 0, 0
    for i in s:
        if (i == 'A' and k % 2 == 0) or (i == 'B' and k % 2 == 1):
            k += 1
            m = max(k, m)
        elif i == 'A':
            k = 1
        else:
            k = 0
    print(m)
