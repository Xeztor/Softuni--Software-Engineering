def stock_availability(inventory, action, *args):
    if action == 'sell':
        inventory = sell(inventory, args)
    elif action == 'delivery':
        inventory = delivey(inventory, args)

    return inventory


def sell(inventory, args):
    args = list(args)
    if not args:
        inventory.pop(0)
    elif isinstance(args[0], int):
        for _ in range(int(args.pop())):
            inventory.pop(0)
            if not inventory:
                break
    else:
        for product in args:
            while product in inventory:
                inventory.remove(product)

    return inventory


def delivey(inventory, args):
    args = list(args)
    inventory.extend(args)

    return inventory
