import numpy

dimens = input().split()
n, m = list(map(int, dimens))

a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))

a = numpy.array(a, int)
b = numpy.array(b, int)

print(a + b)

print(a - b)

print(a * b)

print(a // b)

print(a % b)

print(a ** b)
