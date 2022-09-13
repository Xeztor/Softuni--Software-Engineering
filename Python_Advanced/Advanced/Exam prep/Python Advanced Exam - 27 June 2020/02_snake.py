class SquareMatrix:
    def __init__(self):
        self.matrix = [list(input()) for _ in range(int(input()))]
        self.lairs = self.get_lairs()

    def get_snake_coord(self):
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 'S':
                    return r, c

    def get_lairs(self):
        lairs = []
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                if self.matrix[r][c] == 'B':
                    lairs.append((r, c))

        return lairs

    def get_val(self, row_i, col_i):
        return self.matrix[row_i][col_i]


class Snake:
    def __init__(self, row_i, col_i):
        self.row_i = row_i
        self.col_i = col_i
        self.food_eaten = 0

    def check_move(self, matrix, command):
        x, y = direction_coordinates(command)
        new_row_i = self.row_i + y
        new_col_i = self.col_i + x
        if existing_index(matrix.matrix, new_row_i, new_col_i):
            val_at_index = matrix.get_val(new_row_i, new_col_i)
            if val_at_index == '*':
                return 'eat'
            elif val_at_index == 'B':
                return 'dash'
            else:
                return 'move'
        else:
            return 'died'

    def move(self, matrix, direction):
        x, y = direction_coordinates(direction)
        matrix.matrix[self.row_i][self.col_i] = '.'
        matrix.matrix[self.row_i + y][self.col_i + x] = 'S'
        self.row_i, self.col_i = self.row_i + y, self.col_i + x

    def eat(self):
        self.food_eaten += 1

    def die(self, matrix):
        matrix.matrix[self.row_i][self.col_i] = '.'

    def dash(self, matrix, direction):
        self.move(matrix, direction)
        matrix.lairs.remove((self.row_i, self.col_i))
        new_y, new_x = matrix.lairs[0]
        matrix.matrix[self.row_i][self.col_i] = '.'
        self.row_i = new_y
        self.col_i = new_x
        matrix.matrix[new_y][new_x] = 'S'


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
        row = list(input())
        matrix.append(row)

    return matrix


def print_matrix(matrix):
    [print(''.join(row)) for row in matrix]


my_matrix = SquareMatrix()

snake = Snake(*my_matrix.get_snake_coord())

command = input()
while command:
    move_outcome = snake.check_move(my_matrix, command)

    if move_outcome == 'eat':
        snake.eat()
        snake.move(my_matrix, command)
    elif move_outcome == 'move':
        snake.move(my_matrix, command)
    elif move_outcome == 'dash':
        snake.dash(my_matrix, command)
    elif move_outcome == 'died':
        snake.die(my_matrix)
        print('Game over!')
        break

    if snake.food_eaten >= 10:
        print('You won! You fed the snake.')
        break

    command = input()

print(f'Food eaten: {snake.food_eaten}')
print_matrix(my_matrix.matrix)
