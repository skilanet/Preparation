with open('27690.txt') as f:
    s = f.readline()
    k, maxi = 1, 0
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            k += 1
            maxi = max(k, maxi)
        else:
            k = 1
    print(maxi)