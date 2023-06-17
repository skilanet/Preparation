with open('17.txt') as f:
    l = [int(i) for i in f]
    answ = []
    k = 9973
    for i in range(1, len(l)):
        if (str(l[i - 1])[-1] == '3' and str(l[i])[-1] != '3') or (
                str(l[i])[-1] == '3' and str(l[i - 1])[-1] != '3') and ((l[i] ** 2 + l[i - 1] ** 2) >= k ** 2):
            answ.append(l[i] ** 2 + l[i - 1] ** 2)
    print(len(answ), max(answ))
