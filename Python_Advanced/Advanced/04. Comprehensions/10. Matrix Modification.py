class SquareMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, y, x, val):
        self.matrix[y][x] += val

    def subtract(self, y, x, val):
        self.matrix[y][x] -= val


def read_matrix():
    matrix = []
    rows = int(input())
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def existing_index(matrix, row_i, col_i):
    if row_i in range(len(matrix)) and \
            col_i in range(len(matrix[0])):
        return True
    return


matrix = SquareMatrix(read_matrix())

command = input()
while not command == 'END':
    command, row, col, val = command.split()
    row, col, val = int(row), int(col), int(val)
    if existing_index(matrix.matrix, row, col):
        if command == 'Add':
            matrix.add(row, col, val)
        else:
            matrix.subtract(row, col, val)
    else:
        print('Invalid coordinates')

    command = input()

[print(*row) for row in matrix.matrix]
