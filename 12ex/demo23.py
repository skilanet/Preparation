def is_prime(n):
    l = []
    for i in range(2, round(n ** 0.5) + 1):
        if n % i == 0:
            l.append(i)
            l.append(n // i)
    return len(l) == 0


for n in range(100):
    s = '>' + 39 * '0' + n * '1' + 39 * '2'
    while ('>1' in s) or ('>2' in s) or ('>3' in s):
        if '>1' in s:
            s = s.replace('>1', '22>')
        elif '>2' in s:
            s = s.replace('>2', '2>')
        elif '>0' in s:
            s = s.replace('>0', '1>')
    s = s.replace('>', '')
    if is_prime(sum(map(int, list(s)))):
        print(n)
