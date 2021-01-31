class SquareMatrix:
    def __init__(self, rows):
        self.matrix = [list(input()) for _ in range(rows)]

    def get_player_coord(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 'P':
                    return r, c

    def get_val(self, row_i, col_i):
        return self.matrix[row_i][col_i]


class Player:
    def __init__(self, initial_string, row_i, col_i):
        self.string = initial_string
        self.row_i = row_i
        self.col_i = col_i

    def check_move(self, matrix, command):
        x, y = direction_coordinates(command)
        new_row_i = self.row_i + y
        new_col_i = self.col_i + x
        if existing_index(matrix.matrix, new_row_i, new_col_i):
            val_at_index = matrix.get_val(new_row_i, new_col_i)
            if not val_at_index == '-':
                return 'letter', val_at_index
            else:
                return 'move',
        else:
            return 'penalty',

    def move(self, matrix, direction):
        x, y = direction_coordinates(direction)
        matrix.matrix[self.row_i][self.col_i] = '-'
        matrix.matrix[self.row_i + y][self.col_i + x] = 'P'
        self.row_i, self.col_i = self.row_i + y, self.col_i + x

    def remove_last_letter(self):
        if self.string:
            self.string = ''.join(list(self.string)[:-1])

    def add_letter(self, letter):
        self.string += letter


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


def print_matrix(matrix):
    [print(''.join(row)) for row in matrix.matrix]


initial_s = input()

matrix_rows = int(input())

my_matrix = SquareMatrix(matrix_rows)
player = Player(initial_s, *my_matrix.get_player_coord())

commands = int(input())
for _ in range(commands):
    cmd = input()
    move_outcome, *args = player.check_move(my_matrix, cmd)
    if move_outcome == 'move':
        player.move(my_matrix, cmd)
    elif move_outcome == "letter":
        player.add_letter(args.pop())
        player.move(my_matrix, cmd)
    elif move_outcome == 'penalty':
        player.remove_last_letter()

print(player.string)
print_matrix(my_matrix)