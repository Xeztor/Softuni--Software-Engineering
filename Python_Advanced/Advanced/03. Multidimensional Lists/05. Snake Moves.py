class SnakeWord:
    def __init__(self, word):
        self.word = word[::-1]
        self.word_stack = list(self.word)

    def get_letter(self):
        if not self.word_stack:
            self.word_stack = list(self.word)

        return self.word_stack.pop()


def make_matrix():
    rows, cols = map(int, input().split())
    matrix = []
    for r in range(rows):
        row = [0] * cols
        matrix.append(row)

    return matrix


def print_result(matrix):
    [print(''.join(row)) for row in matrix]


matrix = make_matrix()
snake_word = SnakeWord(input())

for r in range(len(matrix)):
    if r % 2 == 0:
        for c in range(len(matrix[r])):
            matrix[r][c] = snake_word.get_letter()
    else:
        for c in range(len(matrix[r]) - 1, -1, -1):
            matrix[r][c] = snake_word.get_letter()

print_result(matrix)
