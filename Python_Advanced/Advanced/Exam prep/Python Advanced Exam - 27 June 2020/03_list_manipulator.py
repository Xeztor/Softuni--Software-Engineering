def list_manipulator(nums, cmd, param, *args):
    if cmd == 'add':
        return add(nums, param, args)
    elif cmd == 'remove':
        return remove(nums, param, args)


def add(nums, param, args):
    args = list(args)
    if param == 'beginning':
        args.extend(nums)
        return args
    else:
        nums.extend(args)
        return nums


def remove(nums, param, args):
    if args:
        elements_to_remove = args[0]
    else:
        elements_to_remove = 1

    if param == 'beginning':
        for _ in range(elements_to_remove):
            nums.pop(0)
        else:
            return nums
    else:
        for _ in range(elements_to_remove):
            nums.pop()
        else:
            return nums


# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
# print(list_manipulator([1, 2, 3], "remove", "end", 2))
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
