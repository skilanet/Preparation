s = 1000 * '9'
while ('999' in s) or ('888' in s):
    if '888' in s:
        s = s.replace('888', '9')
    if '999' in s:
        s = s.replace('999', '8')

print(s)
