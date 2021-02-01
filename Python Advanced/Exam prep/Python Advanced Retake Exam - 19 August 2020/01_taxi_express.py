from collections import deque


def print_customers(clients):
    print(f"Customers left: {', '.join([str(client) for client in clients])}")


customers = deque(map(int, input().split(', ')))
taxis = list(map(int, input().split(', ')))

total_time = 0

while customers:
    taxi_avlb = taxis.pop()
    if taxi_avlb >= customers[0]:
        total_time += customers.popleft()

    if not taxis and customers:
        print(f'Not all customers were driven to their destinations')
        print_customers(customers)
        break
else:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
