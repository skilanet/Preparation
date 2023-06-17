with open('27689.txt') as f:
    s = f.readline()
    k, maxi = 3, 0
    for i in range(3, len(s), 3):
        if s[i-2] + s[i-1] + s[i] == 'XYZ':
            k += 3
            maxi = max(maxi, k)
        else:
            k = 3
    print(maxi)