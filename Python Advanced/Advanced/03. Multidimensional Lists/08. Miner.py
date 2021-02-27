class SquareMatrix:
    def __init__(self, rows):
        self.matrix = [input().split() for _ in range(rows)]
        self.coals = self.sum_coals()

    def sum_coals(self):
        coals = 0
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 'c':
                    coals += 1

        return coals

    def get_miner_coord(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 's':
                    return r, c

    def get_val(self, row_i, col_i):
        return self.matrix[row_i][col_i]


class Miner:
    def __init__(self, row_i, col_i):
        self.row_i = row_i
        self.col_i = col_i
        self.coals_mined = 0

    def check_move(self, matrix, command):
        x, y = direction_coordinates(command)
        new_row_i = self.row_i + y
        new_col_i = self.col_i + x
        if existing_index(matrix.matrix, new_row_i, new_col_i):
            val_at_index = matrix.get_val(new_row_i, new_col_i)
            if val_at_index == 'c':
                self.coals_mined += 1
                matrix.coals -= 1
                return 'move'
            elif val_at_index == 'e':
                return 'end'
            else:
                return 'move'

    def move(self, matrix, direction):
        x, y = direction_coordinates(direction)
        matrix.matrix[self.row_i][self.col_i] = '*'
        matrix.matrix[self.row_i + y][self.col_i + x] = 's'
        self.row_i, self.col_i = self.row_i + y, self.col_i + x


def direction_coordinates(command):
    x = 0
    y = 0
    if command == 'right':
        x = 1
    elif command == 'left':
        x = -1
    elif command == 'up':
        y = -1
    elif command == 'down':
        y = 1

    return x, y


def existing_index(matrix, row_i, col_i):
    if row_i in range(len(matrix)) and \
            col_i in range(len(matrix[0])):
        return True
    return


def read_matrix():
    rows = int(input())
    matrix = []
    for r in range(rows):
        row = input().split()
        matrix.append(row)

    return matrix


matrix_rows = int(input())

commands = input().split()

my_matrix = SquareMatrix(matrix_rows)
miner = Miner(*my_matrix.get_miner_coord())

for direction in commands:
    move_outcome = miner.check_move(my_matrix, direction)
    if move_outcome == 'end':
        miner.move(my_matrix, direction)
        print(f'Game over!', my_matrix.get_miner_coord())
        break
    elif move_outcome == 'move':
        miner.move(my_matrix, direction)
        if not my_matrix.coals:
            print('You collected all coals!', my_matrix.get_miner_coord())
            break
else:
    if my_matrix.coals:
        print(f'{my_matrix.coals} coals left.', my_matrix.get_miner_coord())
