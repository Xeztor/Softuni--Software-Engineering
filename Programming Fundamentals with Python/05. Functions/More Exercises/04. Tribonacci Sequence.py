def tribonacci(nums_list):

    if not nums_list:
        nums_list.append(1)
    elif len(nums_list) < 3:
        nums_list.append(sum(nums_list))
    else:
        nums_list.append(sum([nums_list[-1], nums_list[-2], nums_list[-3]]))

    return nums_list


n = int(input())

nums = []
for i in range(n):
    tribonacci(nums)

print(" ".join(list(map(str, nums))))
