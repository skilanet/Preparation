for n in range(10):
    s = '>' + 21 * '0' + n * '1' + n * '2'
    while ('>1' in s) or ('>2' in s) or ('>0' in s):
        if '>1' in s:
            s = s.replace('>1', '22>')
        elif '>2' in s:
            s = s.replace('>2', '2>')
        elif '0>' in s:
            s = s.replace('0>', '1>')

    sum = s.count('1') + s.count('2') * 2
    if sum % n == 0:
        print(n)
