from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))

products = product(A, B)

[print(prod, end= ' ') for prod in products]
