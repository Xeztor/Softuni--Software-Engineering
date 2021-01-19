def read_matrix(is_test=False):
    if is_test:
        matrix = [
            ['A', 'B', 'B', 'D'],
            ['A', 'B', 'B', 'B'],
            ['A', 'J', 'B', 'B'],

        ]
    else:
        rows, cols = map(int, input().split())
        matrix = []
        for r in range(rows):
            row = input().split()
            matrix.append(row)

    return matrix


def check_if_submatrix_is_square(matrix, row_i, col_i, size):
    sub_matrix = []
    for r in range(row_i, row_i + size):
        sub_row = matrix[r][col_i:col_i + size]
        if not sub_row[0] == sub_row[1]:
            return
        else:
            sub_matrix.append(sub_row)

    if not sub_matrix[0] == sub_matrix[1]:
        return

    return sub_matrix


SIZE = 2

matrix = read_matrix(is_test=False)
matrix_squares = 0

for r in range(len(matrix) - SIZE + 1):
    for c in range(len(matrix[r]) - SIZE + 1):
        if check_if_submatrix_is_square(matrix, r, c, SIZE):
            matrix_squares += 1

print(matrix_squares)
