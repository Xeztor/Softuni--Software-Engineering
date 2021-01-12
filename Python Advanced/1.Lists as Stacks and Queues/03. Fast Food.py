from collections import deque

food_for_day = int(input())

orders = deque(map(int, input().split()))
print(max(orders))

while orders and orders[0] <= food_for_day:
    food_for_day -= orders.popleft()

if not orders:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join(map(str, orders))}")
