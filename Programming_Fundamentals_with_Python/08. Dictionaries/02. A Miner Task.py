data = input()

resources = {}

while not data == "stop":
    quantity = int(input())
    if data not in resources:
        resources[data] = quantity
    else:
        resources[data] += quantity

    data = input()

for key, value in resources.items():
    print(f'{key} -> {value}')
