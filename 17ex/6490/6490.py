def check(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    if s == s[::-1]:
        return abs(n)
    else:
        return 0


with open('17-370.txt') as f:
    lst = [int(i) for i in f]
    max_v = max(map(check, lst))
    answ = []
    for i in range(1, len(lst)):
        if ((len(str(lst[i - 1])) == 4 and len(str(lst[i])) != 4) or (
                len(str(lst[i])) == 4 and len(str(lst[i - 1])) != 4)) and (lst[i] ** 2 + lst[i - 1] ** 2) % max_v == 0:
            answ.append(lst[i - 1]**2 + lst[i]**2)

    print(len(answ), min(answ))
