from itertools import product, permutations


def f(x, y, z, w):
    return (not (x <= w)) or (y <= z) or (not y)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    t = [(a1, 0, a2, a3), (0, 1, a4, a5), (1, a6, a7, 0)]
    for p in permutations('xyzw'):
        if [f(**dict(zip(p, r))) for r in t] == [0, 0, 0]:
            print(p)
            break
