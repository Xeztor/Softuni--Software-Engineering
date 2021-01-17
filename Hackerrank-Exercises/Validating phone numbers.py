import re

lines = int(input())

for _ in range(lines):
    if re.fullmatch(r'[789]\d{9}', input()):
        print('YES')
    else:
        print('NO')
