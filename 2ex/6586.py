from itertools import product, permutations


def f(x, y, z, w):
    return ((x or y) == (y <= z)) or w


for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    t = [(a1, 1, a2, a3), (a4, a5, a6, 1), (1, a7, a8, 1)]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
            print(p)
            break
