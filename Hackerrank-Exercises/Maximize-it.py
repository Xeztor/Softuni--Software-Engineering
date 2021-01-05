from itertools import product


def f(x):
    return x**2


k, m = list(map(int, input().split()))

all = []

for _ in range(k):
    ni, *digits = list(map(int, input().split()))
    all.append(digits)

print(max([sum(list(map(f, digits))) % m for digits in list(product(*all))]))