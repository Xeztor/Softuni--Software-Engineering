def read_matrix(is_test=False):
    if is_test:
        matrix = [
            [1, 5, 5, 2, 4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2, 8],
            [4, 8, 12, 16, 4],

        ]
    else:
        rows, cols = map(int, input().split())
        matrix = []
        for r in range(rows):
            row = list(map(int, input().split()))
            matrix.append(row)

    return matrix


def check_submatrix_sum(matrix, row_i, col_i, SIZE):
    sub_matrix_sum = 0
    for r in range(row_i, row_i + SIZE):
        for c in range(col_i, col_i + SIZE):
            sub_matrix_sum += matrix[r][c]

    return sub_matrix_sum


def highest_valued_submatrix(matrix, SIZE):
    best_row_i = 0
    best_col_i = 0
    best_sum = 0
    for row_i in range(len(matrix) - SIZE + 1):
        for col_i in range(len(matrix[row_i]) - SIZE + 1):
            crnt_submatrix = check_submatrix_sum(matrix, row_i, col_i, SIZE)
            if crnt_submatrix > best_sum:
                best_sum = crnt_submatrix
                best_row_i = row_i
                best_col_i = col_i
    return best_row_i, best_col_i, best_sum


def print_result(matrix, row_i, col_i, best_sum, SIZE):
    print(f'Sum = {best_sum}')
    best_submatrix = []
    for r in range(row_i, row_i + SIZE):
        best_submatrix.append(matrix[r][col_i:col_i + SIZE])
    [print(*row) for row in best_submatrix]


SIZE = 3

matrix = read_matrix(is_test=False)
(best_row_i, best_col_i, best_sum) = highest_valued_submatrix(matrix, SIZE)
print_result(matrix, best_row_i, best_col_i, best_sum, SIZE)
