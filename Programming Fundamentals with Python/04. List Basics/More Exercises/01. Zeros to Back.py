numbers = input().split(", ")
numbers = list(map(int, numbers))


def move_zeros(nums_list):
    for i in range(nums_list.count(0)):
        nums_list.remove(0)
        nums_list.append(0)

    print(nums_list)


move_zeros(numbers)
