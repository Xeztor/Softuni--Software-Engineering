nums = input().split()
k = int(input())
nums = list(map(int, nums))

permutation = []
crnt_index = 0

for i in range(len(nums)):
    for j in range(k):
        if j == k - 1:
            crnt_index = nums.index(nums[crnt_index])
            permutation.append(nums[crnt_index])
            nums.pop(crnt_index)
        else:
            crnt_index += 1
        if crnt_index >= len(nums):
            crnt_index = 0

print("[", end="")
print(",".join(list(map(str, permutation))), end="")
print("]")
