def read_matrix():
    rows = int(input())
    matrix = []
    for r in range(rows):
        row = [0] * rows
        matrix.append(row)

    return matrix


def change_matrix_for_bomb(matrix, coordinates):
    row_i, col_i = coordinates
    for y in range(-1, 2):
        for x in range(-1, 2):
            try:
                row_clock = row_i + y
                col_clock = col_i + x
                if (row_clock == row_i and col_clock == col_i) or row_clock < 0 or col_clock < 0 or \
                        matrix[row_clock][col_clock] == '*':
                    continue
                matrix[row_clock][col_clock] += 1
            except IndexError:
                continue

    return matrix


def read_bombs_coordinates():
    bomb_num = int(input())
    bombs = []
    for i in range(bomb_num):
        bomb = tuple(map(int, input()[1:-1].split(', ')))
        bombs.append(bomb)
    return bombs


def put_bombs_on_matrix(matrix, *args):
    for coord in args:
        x, y = coord
        if x >= 0 and y >= 0:
            matrix[x][y] = "*"

    return matrix


def print_minefield(minefield):
    [print(' '.join(map(str, row))) for row in minefield]


matrix = read_matrix()
bombs_coordinates = read_bombs_coordinates()
matrix = put_bombs_on_matrix(matrix, *bombs_coordinates)

for coordinates in bombs_coordinates:
    matrix = change_matrix_for_bomb(matrix, coordinates)


print_minefield(matrix)
