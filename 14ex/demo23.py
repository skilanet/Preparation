for i in '0123456789abcde':
    if (int(f'123{i}5', 15) + int(f'1{i}233', 15)) % 14 == 0:
        print((int(f'123{i}5', 15) + int(f'1{i}233', 15)) // 14)