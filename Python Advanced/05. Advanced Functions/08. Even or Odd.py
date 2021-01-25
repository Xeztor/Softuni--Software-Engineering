def even_odd(*args):
    args = list(args)
    command = args.pop()
    if command == 'even':
        return [num for num in args if num % 2 == 0]
    elif command == 'odd':
        return [num for num in args if num % 2 == 1]