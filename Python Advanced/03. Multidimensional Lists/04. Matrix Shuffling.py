def read_matrix():
    rows, cols = map(int, input().split())
    matrix = []
    for r in range(rows):
        row = input().split()
        matrix.append(row)

    return matrix, (rows, cols)


def check_valid_command(command, dimens):
    cmd, *indexes = command.split()
    is_valid = True
    if not cmd == 'swap' or not len(indexes) == 4:
        is_valid = False
    else:
        r1, c1, r2, c2 = list(map(int, indexes))
        for r in [r1, r2]:
            if r >= dimens[0]:
                is_valid = False
                break
        for c in [c1, c2]:
            if c >= dimens[1]:
                is_valid = False
                break

    if is_valid:
        return tuple(map(int, indexes))
    else:
        print('Invalid input!')
        return False


def swap_elements(matrix, r1, c1, r2, c2):
    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
    return matrix


def print_matrix(matrix):
    [print(*row) for row in matrix]


(matrix, dimens) = read_matrix()

cmd = input()
while not cmd == 'END':
    is_command_valid = check_valid_command(cmd, dimens)
    if is_command_valid:
        matrix = swap_elements(matrix, *is_command_valid)
        print_matrix(matrix)

    cmd = input()
