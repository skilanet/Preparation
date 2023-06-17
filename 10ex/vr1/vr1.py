with open('dubrovskiy.txt') as f:
    k = 0
    s = f.read().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').lower().split()
    for i in s:
        if 'пир' in i:
            k += 1
            print(i)
    print(k)