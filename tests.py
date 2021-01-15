from collections import deque

food_quantity = int(input())
order_queue = deque(map(int, input().split()))

BIGGEST_ORDER = -1

left_orders = ""
for i in range(len(order_queue)):
    current_order = order_queue.popleft()

    if food_quantity - current_order >= 0:
        food_quantity -= current_order
        if current_order > BIGGEST_ORDER:
            BIGGEST_ORDER = current_order

    else:
        order_queue.append(current_order)
        break

print(BIGGEST_ORDER)

if len(order_queue) == 0:
    print("Orders complete")

else:
    for i in range(len(order_queue)):
        left_orders += str(order_queue[i]) + " "
    print(f"Orders left: {left_orders}")
