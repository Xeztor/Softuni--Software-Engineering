def read_matrix(is_test=False):
    if is_test:
        matrix = [
            [8, 3, 2, 5],
            [6, 4, 7, 9],
            [9, 9, 3, 6],
            [6, 8, 1, 2],
        ]
    else:
        rows = int(input())
        matrix = []
        for r in range(rows):
            row = list(map(int, input().split()))
            matrix.append(row)

    return matrix


def explode_bomb(matrix, coordinates):
    row_i, col_i = coordinates
    bomb_value = matrix[row_i][col_i]
    if bomb_value > 0:
        for y in range(-1, 2):
            for x in range(-1, 2):
                try:
                    row_clock = row_i + y
                    col_clock = col_i + x
                    if matrix[row_i + y][col_i + x] > 0 and \
                            row_clock >= 0 and \
                            col_clock >= 0:
                        matrix[row_i + y][col_i + x] -= bomb_value
                except IndexError:
                    continue

    return matrix


def sum_alive(matrix):
    total_sum = 0
    for r in range(len(matrix)):
        total_sum += sum([val for val in matrix[r] if val > 0])

    return total_sum


def alive_cells_count(matrix):
    alive_cells = 0
    for r in range(len(matrix)):
        alive_cells += sum([1 for val in matrix[r] if val > 0])

    return alive_cells


def print_result(alive_cells, sum_cells, matrix):
    print(f'Alive cells: {alive_cells}')
    print(f'Sum: {sum_cells}')
    [print(*row) for row in matrix]


matrix = read_matrix(is_test=False)

bombs = input().split(' ')

for bomb in bombs:
    coordinates = list(map(int, bomb.split(',')))
    matrix = explode_bomb(matrix, coordinates)

alive_cells = alive_cells_count(matrix)
sum_alive_cells = sum_alive(matrix)

print_result(alive_cells, sum_alive_cells, matrix)