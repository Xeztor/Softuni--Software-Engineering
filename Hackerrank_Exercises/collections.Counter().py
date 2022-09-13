from collections import Counter

pairs_count = int(input())

sizes = list(map(int, input().split()))

stock = Counter(sizes)

profit = 0

customers = int(input())

for _ in range(customers):
    size, price = list(map(int, input().split()))
    if stock[size]:
         stock[size] -= 1
         profit += price

print(profit)