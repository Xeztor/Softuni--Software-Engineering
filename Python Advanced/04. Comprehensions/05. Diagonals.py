def read_matrix():
    matrix = []
    rows = int(input())
    for _ in range(rows):
        row = list(map(int, input().split(', ')))
        matrix.append(row)
    return matrix


matrix = read_matrix()
primary_diagonal = [matrix[n][n] for n in range(len(matrix))]
print(f"First diagonal: {', '.join(list(map(str, primary_diagonal)))}. Sum: {sum(primary_diagonal)}")
secondary_diagonal = [matrix[n][len(matrix) - n - 1] for n in range(len(matrix))]
print(f"Second diagonal: {', '.join(list(map(str, secondary_diagonal)))}. Sum: {sum(secondary_diagonal)}")
