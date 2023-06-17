from itertools import product, permutations


def f1(x, y, z, w):
    return (w <= y) == (z <= x)


def f2(x, y, z, w):
    return (w <= y) and ((not x) == z)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    t = [(0, a1, 0, 0), (0, 0, 0, a2), (0, 1, 1, a3)]
    for p in permutations('xyzw'):
        if [f1(**dict(zip(p, r))) for r in t] == [0, 0, a4] and [f2(**dict(zip(p, r))) for r in t] == [1, a5, 0]:
            print(p)
            break
