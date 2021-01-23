class BunniesMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.bunnies = self.get_bunnies()

    def get_player_coord(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 'P':
                    return r, c

    def get_bunnies(self):
        bunnies = []
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 'B':
                    bunnies.append((r, c))
        return bunnies

    def get_val(self, row_i, col_i):
        return self.matrix[row_i][col_i]

    def update(self):
        new_bunnies = []
        for row_i, col_i in self.bunnies:
            for x in range(-1, 2, 2):
                if existing_index(self.matrix, row_i, col_i + x):
                    self.matrix[row_i][col_i + x] = 'B'
                    new_bunnies.append((row_i, col_i + x))

            for y in range(-1, 2, 2):
                if existing_index(self.matrix, row_i + y, col_i):
                    self.matrix[row_i + y][col_i] = 'B'
                    new_bunnies.append((row_i + y, col_i))

        self.bunnies = new_bunnies


class Player:
    def __init__(self, row_i, col_i):
        self.row_i = row_i
        self.col_i = col_i

    def get_coordinates(self):
        return self.row_i, self.col_i

    def check_move(self, matrix, command):
        x, y = direction_coordinates(command)
        new_row_i = self.row_i + y
        new_col_i = self.col_i + x
        if existing_index(matrix.matrix, new_row_i, new_col_i):
            val_at_index = matrix.get_val(new_row_i, new_col_i)
            if val_at_index == '.':
                self.move(matrix, command)
            elif val_at_index == 'B':
                return 'end'
        else:
            return 'escaped'

    def move(self, matrix, direction):
        x, y = direction_coordinates(direction)
        matrix.matrix[self.row_i][self.col_i] = '.'
        matrix.matrix[self.row_i + y][self.col_i + x] = 'P'
        self.row_i, self.col_i = self.row_i + y, self.col_i + x

    def is_alive(self, matrix):
        if matrix.matrix[self.row_i][self.col_i] == 'P':
            return True
        return False

    def escaped(self, matrix):
        matrix.matrix[self.row_i][self.col_i] = '.'

    def died(self, matrix):
        matrix.matrix[self.row_i][self.col_i] = 'B'


def direction_coordinates(command):
    x = 0
    y = 0
    if command == 'R':
        x = 1
    elif command == 'L':
        x = -1
    elif command == 'U':
        y = -1
    elif command == 'D':
        y = 1

    return x, y


def existing_index(matrix, row_i, col_i):
    if row_i in range(len(matrix)) and \
            col_i in range(len(matrix[0])):
        return True
    return


def read_matrix():
    rows, cols = map(int, input().split())
    print(rows)
    matrix = []
    for r in range(rows):
        row = list(input())
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    [print(''.join(row)) for row in matrix.matrix]


my_matrix = BunniesMatrix(read_matrix())
player = Player(*my_matrix.get_player_coord())

commands = input()

for command in commands:
    is_dead = False
    is_escaped = False
    step_outcome = player.check_move(my_matrix, command)
    if step_outcome == 'end':
        is_dead = True
        player.move(my_matrix, command)
    elif step_outcome == 'escaped':
        is_escaped = True

    if is_escaped:
        player.escaped(my_matrix)
        my_matrix.update()
        print_matrix(my_matrix)
        print(f"won: {' '.join(map(str, player.get_coordinates()))}")
        break

    my_matrix.update()

    if not player.is_alive(my_matrix):
        is_dead = True

    if is_dead:
        player.died(my_matrix)
        print_matrix(my_matrix)
        print(f"dead: {' '.join(map(str, player.get_coordinates()))}")
        break
