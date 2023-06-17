with open('10.txt') as f:
    s = f.read()
    d = [',', '.', '!', '?']
    k = 0
    for i in d:
        s = s.replace(i, ' ')
    lst = s.split()
    for i in lst:
        if i == 'теперь':
            k += 1
    print(k)
