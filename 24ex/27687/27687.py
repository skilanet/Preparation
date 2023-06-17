with open('27687.txt') as f:
    s = f.readline().replace('X', ' ').replace('Z', ' ').split()
    print(max(map(len, s)))