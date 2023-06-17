def f(pos, end):
    if pos > end:
        return 0
    elif pos == end:
        return 1
    else:
        return f(pos + 1, end) + f(pos * 2, end)


print(f(1, 10) + f(10, 15) + f(18, 35))
