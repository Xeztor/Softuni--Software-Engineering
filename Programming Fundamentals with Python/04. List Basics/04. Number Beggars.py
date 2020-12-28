nums = input()
beggers = int(input())

list_nums = list(map(int, nums.split(", ")))

result = []

for i in range(beggers):
    if i >= len(list_nums):
        result.append(0)
        continue
    if i + beggers <= len(list_nums) - 1 and i < len(list_nums):
        crnt_sum = 0
        for j in range(i, len(list_nums), beggers):
            crnt_sum += list_nums[j]
        result.append(crnt_sum)
    else:
        result.append(list_nums[i])

print(result)
