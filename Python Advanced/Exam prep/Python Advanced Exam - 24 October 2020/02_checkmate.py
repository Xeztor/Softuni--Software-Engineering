DIRECTIONS_MAPPER = {
        'up': (-1, 0),
        'down': (1, 0),
        'right': (0, 1),
        'left': (0, -1),
        'left_top': (-1, -1),
        'right_top': (-1, 1),
        'right_down': (1, 1),
        'left_down': (1, -1),
    }


class ChessBoard:
    def __init__(self, matrix_state):
        self.matrix = matrix_state
        self.queens_coords = self.get_queens_coordinates()

    def get_queens_coordinates(self):
        queens_coords = []
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 'Q':
                    queens_coords.append((r, c))

        return queens_coords


def read_matrix():
    matrix = []
    for _ in range(8):
        row = list(input().split())
        matrix.append(row)

    return matrix


def check_direction(direction):
    return DIRECTIONS_MAPPER[direction]


def recursive_search_for_king(matrix, direction, *queen_coord, depth=0):
    queen_y, queen_x = queen_coord

    if matrix[queen_y][queen_x] == 'Q' and depth > 0:
        return False
    elif matrix[queen_y][queen_x] == 'K':
        return True

    y, x = check_direction(direction)

    if existing_index(matrix, queen_y + y, queen_x + x):
        return recursive_search_for_king(matrix, direction, *(queen_y + y, queen_x + x), depth=1)
    else:
        return False


def check_queen_if_killer(matrix, row, col):
    results = []
    for direction in DIRECTIONS_MAPPER:
        is_killer_in_direction = recursive_search_for_king(matrix, direction, *(row, col))
        if is_killer_in_direction:
            results.append(is_killer_in_direction)

    return any(results)


def existing_index(matrix, row_i, col_i):
    if len(matrix) > row_i >= 0 and \
            len(matrix) > col_i >= 0:
        return True
    return False


matrix = read_matrix()
board = ChessBoard(matrix)

killers = []

for r, c in board.queens_coords:
    if check_queen_if_killer(board.matrix, r, c):
        killers.append([r, c])

if killers:
    [print(killer) for killer in killers]
else:
    print('The king is safe!')
