def shoot(targs, index, power):
    if index in range(0, len(targs)):
        if targs[index] - power < 1:
            targs.pop(index)
        else:
            targs[index] -= power

    return targs


def add_target(targs, index, value):
    if index in range(0, len(targs)):
        targs.insert(index, value)
    else:
        print("Invalid placement!")

    return targs


def strike(targs, index, radius):
    if index - radius in range(0, len(targs)) and index + radius in range(0, len(targs)):
        del targs[index-radius:index + radius + 1]
    else:
        print("Strike missed!")

    return targs


targets = input().split()
targets = list(map(int, targets))

command = input().split()
while not command[0] == "End":
    if command[0] == "Shoot":
        targets = shoot(targets, int(command[1]), int(command[2]))
    elif command[0] == "Add":
        targets = add_target(targets, int(command[1]), int(command[2]))
    elif command[0] == "Strike":
        targets = strike(targets, int(command[1]), int(command[2]))
    command = input().split()

print("|".join(list(map(str, targets))))
