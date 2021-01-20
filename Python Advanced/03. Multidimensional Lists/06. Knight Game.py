def read_matrix():
    rows = int(input())
    matrix = []
    for r in range(rows):
        row = list(input())
        matrix.append(row)

    return matrix


def check_ls(matrix, row_i, col_i):
    conflicts = 0
    for x in range(-2, 3):
        try:
            if x in [-2, 2]:
                for y in range(-1, 2, 2):
                    row_l = row_i + y
                    col_l = col_i + x
                    if matrix[row_l][col_l] == 'K' and col_l >= 0 and row_l >= 0:
                        conflicts += 1

            elif x in [-1, 1]:
                for y in range(-2, 3, 4):
                    row_l = row_i + y
                    col_l = col_i + x
                    if matrix[row_l][col_l] == 'K' and col_l >= 0 and row_l >= 0:
                        conflicts += 1

        except IndexError:
            continue

    return conflicts


matrix = read_matrix()

knights_removed = 0
max_conflicts = 0

while max_conflicts is not None:
    max_conflicts_row = 0
    max_conflicts_col = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'K':
                check_l = check_ls(matrix, r, c)
                if check_l > max_conflicts:
                    max_conflicts = check_l
                    max_conflicts_row = r
                    max_conflicts_col = c

    if max_conflicts:
        matrix[max_conflicts_row][max_conflicts_col] = '0'
        knights_removed += 1
        max_conflicts = 0
        max_conflicts_row = 0
        max_conflicts_col = 0
    else:
        max_conflicts = None

print(knights_removed)

