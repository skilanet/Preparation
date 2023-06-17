from itertools import product, permutations


def f(x, y, z, w):
    return ((x <= y) == (z <= w)) or (x and w)


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    t = [(1, a1, a2, a3), (1, 1, a4, a5), (1, 1, 1, a6)]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
            print(p)
            break
