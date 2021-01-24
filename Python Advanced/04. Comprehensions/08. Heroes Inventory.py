heroes = input().split(', ')
heroes_data = {name: {} for name in heroes}

command = input()
while not command == 'End':
    name, item, price = command.split('-')
    if item not in heroes_data[name]:
        heroes_data[name][item] = int(price)
    command = input()

for name, items in heroes_data.items():
    items_cost = sum([price for item, price in items.items()])
    print(f'{name} -> Items: {len(items)}, Cost: {items_cost}')

