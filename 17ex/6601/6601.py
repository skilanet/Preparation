with open('17-376.txt') as f:
    lst = [int(i) for i in f]
    k = 0
    answ = []
    for i in lst:
        if hex(i).endswith('0f') and i > k:
            k = i
    for i in range(1, len(lst)):
        if (lst[i-1]%7 == 0 or lst[i]%7 == 0) and (lst[i-1] + lst[i]) % k == 0:
            answ.append(lst[i-1] + lst[i])
    print(len(answ), max(answ))