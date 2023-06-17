with open('24.txt') as f:
    s = f.readline().replace('C', 'S').replace('D', 'S').replace('F', 'S')
    s = s.replace('A', 'G').replace('O', 'G')
    s = s.replace('GS', '*')
    k, k_max = 0, 0
    for i in s:
        if i == '*':
            k += 1
            k_max = max(k, k_max)
        else:
            k = 0
    print(k_max)