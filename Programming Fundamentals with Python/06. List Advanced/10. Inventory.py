def collect(inventory, item):
    if item not in inventory:
        inventory.append(item)

    return inventory


def drop(inventory, item):
    if item in inventory:
        inventory.remove(item)

    return inventory


def combine(inventory, old_item, new_item):
    if old_item in inventory:
        inventory.insert(inventory.index(old_item) + 1, new_item)

    return inventory


def renew_inv(inventory, item):
    if item in inventory:
        item_to_move = inventory.pop(inventory.index(item))
        inventory.append(item_to_move)

    return inventory


items = input().split(", ")

cmd = input().split(" - ")
while not cmd[0] == "Craft!":
    command, value = cmd
    if command == "Collect":
        items = collect(items, value)
    elif command == "Drop":
        items = drop(items, value)
    elif command == "Combine Items":
        old_item, new_item = value.split(":")
        items = combine(items, old_item, new_item)
    elif command == "Renew":
        items = renew_inv(items, value)

    cmd = input().split(" - ")

print(", ".join(items))
