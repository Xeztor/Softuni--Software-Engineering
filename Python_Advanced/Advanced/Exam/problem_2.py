from math import floor


class SquareMatrix:
    def __init__(self, rows):
        self.matrix = [input().split() for _ in range(rows)]

    def get_player_coord(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 'P':
                    return r, c

    def get_val(self, row_i, col_i):
        return self.matrix[row_i][col_i]


class Player:
    def __init__(self, row_i, col_i):
        self.row_i = row_i
        self.col_i = col_i
        self.coins = 0
        self.trail = []

    def check_move(self, matrix, command):
        x, y = direction_coordinates(command)
        new_row_i = self.row_i + y
        new_col_i = self.col_i + x
        if existing_index(matrix.matrix, new_row_i, new_col_i):
            val_at_index = matrix.get_val(new_row_i, new_col_i)
            if val_at_index.isdigit():
                return 'collect', int(val_at_index)
            elif val_at_index == 'X':
                return 'lose',
        else:
            return 'lose',

    def move(self, direction):
        x, y = direction_coordinates(direction)
        self.row_i, self.col_i = self.row_i + y, self.col_i + x
        self.trail.append([self.row_i, self.col_i])

    def collect(self, coins):
        self.coins += coins


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


def print_path(player):
    print('Your path:')
    for coordinates in player.trail:
        print(coordinates)


matrix_rows = int(input())

my_matrix = SquareMatrix(matrix_rows)

player = Player(*my_matrix.get_player_coord())

while True:
    cmd = input()
    if not cmd:
        break

    move_outcome, *args = player.check_move(my_matrix, cmd)
    if move_outcome == 'move':
        player.move(cmd)
    elif move_outcome == 'collect':
        player.collect(args.pop())
        player.move(cmd)
    elif move_outcome == 'lose':
        print(f"Game over! You've collected {floor(player.coins * 0.5)} coins.")
        break
        
    if player.coins >= 100:
        print(f"You won! You've collected {player.coins} coins.")
        break

print_path(player)
