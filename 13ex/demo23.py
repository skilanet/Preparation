s = 'абг бд вабгд геж деил евл же ил кж лжк'
d = {c[0]: c[1:] for c in s.split()}


def f(s, end):
    if s[-1] == end: return 1
    else: return sum(f(s + c, end) for c in d[s[-1]])


print(f('в', 'е') + f('л', 'е'))
