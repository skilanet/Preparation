with open('26.txt') as f:
    n, *l = f.readlines()
    l = sorted(map(int, l), reverse=True)
    k, mini = 0, l[0]
    for i in range(1, len(l)):
        if l[i] + 3 <= mini:
            mini = l[i]
            k += 1
print(k, mini)