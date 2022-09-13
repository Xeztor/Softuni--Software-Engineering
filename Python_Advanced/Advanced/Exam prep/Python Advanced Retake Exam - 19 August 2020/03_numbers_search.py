def numbers_searching(*args):
    args = sorted(args)

    missing = None
    duplicate = []

    for i in range(len(args)):

        if args.count(args[i]) > 1 and args[i] not in duplicate:
            duplicate.append(args[i])

        if not i == 0 and\
                not args[i] - 1 == args[i-1] and\
                not args[i] == args[i - 1]:
            missing = args[i] - 1

    return [missing, duplicate]


print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
