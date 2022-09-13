import numpy

n = int(input())

entries = []

for _ in range(n):
    entries.append(list(map(float, input().split())))

matrix = numpy.array(entries).reshape(n, n)

determinant = numpy.linalg.det(matrix)

print(determinant if len(str(determinant).split('.')[1]) < 3 else f'{determinant:.2f}')

