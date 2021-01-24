FIRST_LETTER = 97

rows, cols = list(map(int, input().split()))
matrix = []

for r in range(rows):
    matrix.append([f'{chr(FIRST_LETTER + r + c)}'.center(3, f'{chr(FIRST_LETTER + r)}') for c in range(cols)])

[print(*row) for row in matrix]
