from fnmatch import fnmatch


def f(n):
    return sum(map(int, list(str(n))))


for i in range(2023, 10 ** 9, 2023):
    if fnmatch(str(i), '20*23') and f(i) % 7 == 0 and f(i) < 20:
        print(i, i // 2023)
