def read_matrix():
    matrix = []
    for _ in range(int(input())):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix


def sum_primary_diagonal(matrix):
    the_sum = 0
    for r in range(len(matrix)):
        the_sum += matrix[r][r]

    return the_sum


def sum_secondary_diagonal(matrix):
    the_sum = 0
    for row_index in range(len(matrix)):
        the_sum += matrix[row_index][len(matrix) - row_index - 1]

    return the_sum


matrix = read_matrix()
primary_sum = sum_primary_diagonal(matrix)
secondary_sum = sum_secondary_diagonal(matrix)
print(abs(primary_sum - secondary_sum))
