def exchange(nums_list, split_index):
    splitted_list = []
    if split_index >= len(nums_list) or split_index < 0:
        print("Invalid index")
        return nums_list

    nums_list = list(map(str, nums_list))
    splitted_list += nums_list[split_index + 1:]
    splitted_list += nums_list[:split_index + 1]

    return list(map(int, splitted_list))


def min_max(nums_list, type_of_filter, type_of_num):
    nums = []

    if type_of_num == "even":
        for i in nums_list:
            if i % 2 == 0:
                nums.append(i)
    elif type_of_num == "odd":
        for i in nums_list:
            if not i % 2 == 0:
                nums.append(i)

    if not nums:
        return "No matches"

    lowest = min(nums)
    highest = max(nums)
    if type_of_filter == "min":
        for i in range(len(nums_list) - 1, -1, -1):
            if nums_list[i] == lowest and (type_of_num == "even" and nums_list[i] % 2 == 0):
                return i
            elif nums_list[i] == lowest and (type_of_num == "odd" and not nums_list[i] % 2 == 0):
                return i
    else:
        for i in range(len(nums_list) - 1, -1, -1):
            if nums_list[i] == highest and (type_of_num == "even" and nums_list[i] % 2 == 0):
                return i
            elif nums_list[i] == highest and (type_of_num == "odd" and not nums_list[i] % 2 == 0):
                return i


def first_last(nums_list, type_of_operation, count_times, type_of_num):
    nums = []
    if count_times > len(nums_list):
        return "Invalid count"
    if type_of_num == "even":
        for i in nums_list:
            if i % 2 == 0:
                nums.append(i)
    elif type_of_num == "odd":
        for i in nums_list:
            if not i % 2 == 0:
                nums.append(i)
    if nums:
        if type_of_operation == "first":
            if len(nums) < count_times:
                return nums
            else:
                return nums[:count_times]
        elif type_of_operation == "last":
            if len(nums) < count_times:
                return nums
            else:
                return nums[-count_times:]
    else:
        return []


raw_data = input().split()
data_map = list(map(int, raw_data))

command = input().split()
while "end" not in command:
    if command[0] == "exchange":
        data_map = exchange(data_map, int(command[1]))
    elif command[0] == "max" or command[0] == "min":
        print(min_max(data_map, command[0], command[1]))
    elif command[0] == "first" or command[0] == "last":
        print(first_last(data_map, command[0], int(command[1]), command[2]))

    command = input().split()

print(data_map)
